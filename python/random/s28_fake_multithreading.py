
import enum
import collections

from typing import Dict, List, Any


@enum.unique
class InstructionCode(enum.IntEnum):
    NOOP = enum.auto()
    DEF = enum.auto()
    SET = enum.auto()
    CP = enum.auto()
    PRINT = enum.auto()
    ADD = enum.auto()
    SUB = enum.auto()
    LT = enum.auto()
    EQ = enum.auto()
    GT = enum.auto()
    AND = enum.auto()
    OR = enum.auto()

    JMP = enum.auto()
    JMPI = enum.auto()
    CMP = enum.auto()
    LABEL = enum.auto()


Instruction = collections.namedtuple('Instruction', ['code', 'args'])


def noop_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    pass


def def_set_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 2
    assert type(instr_args[0]) == str
    context[instr_args[0]] = instr_args[1]


def cp_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 2
    assert type(instr_args[0]) == str
    assert type(instr_args[1]) == str
    context[instr_args[1]] = context[instr_args[0]]


def print_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 2
    assert type(instr_args[0]) == bool

    is_literal = instr_args[0]
    if is_literal:
        value = instr_args[1]
    else:
        value = context[instr_args[1]]

    print("PRINT", value)


def add_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    context[instr_args[2]] = context[instr_args[0]] + context[instr_args[1]]


def sub_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    context[instr_args[2]] = context[instr_args[0]] - context[instr_args[1]]


def lt_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 3
    assert type(instr_args[0]) == str
    assert type(instr_args[1]) == str
    assert type(instr_args[2]) == str

    context[instr_args[2]] = context[instr_args[0]] < context[instr_args[1]]


def eq_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 3
    assert type(instr_args[0]) == str
    assert type(instr_args[1]) == str
    assert type(instr_args[2]) == str

    context[instr_args[2]] = context[instr_args[0]] == context[instr_args[1]]


def gt_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 3
    assert type(instr_args[0]) == str
    assert type(instr_args[1]) == str
    assert type(instr_args[2]) == str

    context[instr_args[2]] = context[instr_args[0]] > context[instr_args[1]]


def and_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 3
    assert type(instr_args[0]) == str
    assert type(instr_args[1]) == str
    assert type(instr_args[2]) == str

    context[instr_args[2]] = context[instr_args[0]] and context[instr_args[1]]


def or_handler(
    instr_args: List[Any],
    context: Dict[str, Any]
) -> None:
    assert len(instr_args) == 3
    assert type(instr_args[0]) == str
    assert type(instr_args[1]) == str
    assert type(instr_args[2]) == str

    context[instr_args[2]] = context[instr_args[0]] or context[instr_args[1]]


HANDLERS = {
    InstructionCode.NOOP: noop_handler,
    InstructionCode.DEF: def_set_handler,
    InstructionCode.SET: def_set_handler,
    InstructionCode.CP: cp_handler,
    InstructionCode.PRINT: print_handler,
    InstructionCode.ADD: add_handler,
    InstructionCode.SUB: sub_handler,
    InstructionCode.LT: lt_handler,
    InstructionCode.EQ: eq_handler,
    InstructionCode.GT: gt_handler,
    InstructionCode.AND: and_handler,
    InstructionCode.OR: or_handler,
}


def jmp_handler(
    instr_args: List[Any],
    instr_index: int,
    labels: Dict[str, int],
    context: Dict[str, Any]
) -> int:
    assert len(instr_args) == 1
    assert type(instr_args[0]) == str

    label_index = labels[instr_args[0]]
    return label_index + 1  # right after the label


def jmpi_handler(
    instr_args: List[Any],
    instr_index: int,
    labels: Dict[str, int],
    context: Dict[str, Any]
) -> int:
    assert len(instr_args) == 1
    assert type(instr_args[0]) == int

    return instr_args[0]


def cmp_handler(
    instr_args: List[Any],
    instr_index: int,
    labels: Dict[str, int],
    context: Dict[str, Any]
) -> int:
    assert len(instr_args) == 1
    assert type(instr_args[0]) == str

    if context[instr_args[0]]:
        return instr_index + 1
    else:
        return instr_index + 2


def label_handler(
    instr_args: List[Any],
    instr_index: int,
    labels: Dict[str, int],
    context: Dict[str, Any]
) -> int:
    assert len(instr_args) == 1
    assert type(instr_args[0]) == str

    labels[instr_args[0]] = instr_index
    return instr_index + 1


CTRL_HANDLERS = {
    InstructionCode.JMP: jmp_handler,
    InstructionCode.JMPI: jmpi_handler,
    InstructionCode.CMP: cmp_handler,
    InstructionCode.LABEL: label_handler,
}


def execute_threads(
    threads: List[List[Instruction]]
) -> None:

    thread_icount: Dict[int, int] = {}
    thread_imax: Dict[int, int] = {}
    thread_context: Dict[int, Dict[str, Any]] = {}
    thread_labels: Dict[int, Dict[str, int]] = {}

    # initialize threads metainfo and context
    for i in range(len(threads)):
        thread_icount[i] = 0
        thread_imax[i] = len(threads[i])
        thread_context[i] = {}
        thread_labels[i] = {}

    # execute threads
    has_instr = True

    while has_instr:
        has_instr = False

        for i in range(len(threads)):
            # check for any instructions
            instr_index = thread_icount[i]
            if instr_index >= thread_imax[i]:
                continue
            else:
                has_instr = True

            # pick instr
            instr = threads[i][instr_index]

            # retrieve context
            context = thread_context[i]

            # retrieve labels
            labels: Dict[str, int] = thread_labels[i]

            print(f"T{i}", instr_index, instr.code.name, instr.args)

            # regular instruction
            if instr.code in HANDLERS:
                instr_handler = HANDLERS[instr.code]
                instr_handler(instr.args, context)
                thread_icount[i] += 1

            # control instruction
            else:
                contr_instr_handler = CTRL_HANDLERS[instr.code]
                thread_icount[i] = contr_instr_handler(
                    instr.args, instr_index, labels, context,
                )


def main() -> None:
    # create some threads
    thread_1 = [
        Instruction(InstructionCode.DEF, ['a', 11]),
        Instruction(InstructionCode.DEF, ['b', 22]),
        Instruction(InstructionCode.PRINT, [False, 'a']),
        Instruction(InstructionCode.PRINT, [False, 'b']),
        Instruction(InstructionCode.SET, ['a', 33]),
        Instruction(InstructionCode.SET, ['a', 44]),
        Instruction(InstructionCode.PRINT, [False, 'a']),
        Instruction(InstructionCode.PRINT, [False, 'b']),
    ]

    thread_2 = [
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.PRINT, [True, "Kogaion"]),
        Instruction(InstructionCode.DEF, ['a', 777]),
        Instruction(InstructionCode.DEF, ['b', 888]),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.PRINT, [False, 'a']),
        Instruction(InstructionCode.PRINT, [False, 'b']),
    ]

    thread_3 = [
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),
        Instruction(InstructionCode.NOOP, []),

        Instruction(InstructionCode.DEF, ['x', None]),
        Instruction(InstructionCode.DEF, ['y', None]),
        Instruction(InstructionCode.SET, ['x', 123]),
        Instruction(InstructionCode.SET, ['y', 987]),
        Instruction(InstructionCode.PRINT, [False, 'x']),
        Instruction(InstructionCode.PRINT, [False, 'y']),
        Instruction(InstructionCode.CP, ['x', 'y']),
        Instruction(InstructionCode.PRINT, [False, 'x']),
        Instruction(InstructionCode.PRINT, [False, 'y']),

        Instruction(InstructionCode.DEF, ['z', 0]),
        Instruction(InstructionCode.SET, ['x', 11]),
        Instruction(InstructionCode.SET, ['y', 22]),
        Instruction(InstructionCode.ADD, ['x', 'y', 'z']),
        Instruction(InstructionCode.PRINT, [False, 'z']),

        Instruction(InstructionCode.SET, ['x', 3]),
        Instruction(InstructionCode.SUB, ['z', 'x', 'z']),
        Instruction(InstructionCode.PRINT, [False, 'z']),

        Instruction(InstructionCode.DEF, ['res', None]),
        Instruction(InstructionCode.DEF, ['i', 0]),
        Instruction(InstructionCode.DEF, ['REF', 10]),
        Instruction(InstructionCode.LT, ['i', 'REF', 'res']),
        Instruction(InstructionCode.PRINT, [False, 'res']),
        Instruction(InstructionCode.EQ, ['i', 'REF', 'res']),
        Instruction(InstructionCode.PRINT, [False, 'res']),

        Instruction(InstructionCode.DEF, ['k', True]),
        Instruction(InstructionCode.CMP, ['k']),
        Instruction(InstructionCode.PRINT, [True, 'foxtrot']),
        Instruction(InstructionCode.PRINT, [True, 'alpha']),

        Instruction(InstructionCode.SET, ['k', False]),
        Instruction(InstructionCode.CMP, ['k']),
        Instruction(InstructionCode.PRINT, [True, 'megasplash']),
        Instruction(InstructionCode.PRINT, [True, 'jupiter']),

        Instruction(InstructionCode.JMPI, [42]),  # 40
        Instruction(InstructionCode.PRINT, [True, 'venus']),  # 41
        Instruction(InstructionCode.PRINT, [True, 'mars']),  # 42

        Instruction(InstructionCode.SET, ['k', True]),  # 43
        Instruction(InstructionCode.CMP, ['k']),
        Instruction(InstructionCode.JMPI, [47]),
        Instruction(InstructionCode.JMPI, [49]),  # 46

        # if
        Instruction(InstructionCode.PRINT, [True, 'black']),  # 47
        Instruction(InstructionCode.JMPI, [50]),  # 48
        # else
        Instruction(InstructionCode.PRINT, [True, 'white']),  # 49

        # for loop
        Instruction(InstructionCode.DEF, ['INC_VAL', 1]),  # 50
        Instruction(InstructionCode.SET, ['i', 0]),  # 51
        Instruction(InstructionCode.SET, ['REF', 10]),  # 52
        Instruction(InstructionCode.LT, ['i', 'REF', 'res']),  # 53
        Instruction(InstructionCode.CMP, ['res']),  # 54
        Instruction(InstructionCode.JMPI, [57]),  # 55
        Instruction(InstructionCode.JMPI, [60]),  # 56
        Instruction(InstructionCode.PRINT, [True, 'yahoo']),  # 57
        Instruction(InstructionCode.ADD, ['i', 'INC_VAL', 'i']),  # 58
        Instruction(InstructionCode.JMPI, [53]),  # 59
        Instruction(InstructionCode.PRINT, [True, "DONE"]),  # 60
    ]

    execute_threads([
        thread_1,
        thread_2,
        thread_3,
    ])


if __name__ == '__main__':
    main()
