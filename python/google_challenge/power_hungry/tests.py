
import pytest
import random

from power_hungry import solution


# i1 = [2, 0, 2, 2, 0]  # 8
# i2 = [-2, -3, 4, -5]  # 60
# i3 = [2, -3, 1, 0, -5] # 30
# i4 = [0, 0, 0, 0, 0]
#
# i5 = [random.randint(-1000, 1000) for _ in range(50)]
# i6 = [-2, -3, 4, -5, -1]
# i7 = [-5] # 0
# i8 = [-5, -2] # 10
# i9 = [0,1,1,1,-2, 1,1,1,2,0,-3]
# i10 = [0, 0, 0, 0, -2]
#
# print solution(i10)

def test_case_1():
    input = [2, -3, 1, 0, -5]
    output = solution(input)
    assert output == "30"

def test_case_2():
    input = [2, 0, 2, 2, 0]
    output = solution(input)
    assert output == "8"

def test_case_3():
    input = [-2, -3, 4, -5]
    output = solution(input)
    assert output == "60"

def test_case_4():
    input = []

    with pytest.raises(AssertionError):
        solution(input)

def test_case_5():
    input = [0, 0, 0, 0, 0]
    output = solution(input)
    assert output == "0"

def test_case_6():
    input = [1]
    output = solution(input)
    assert output == "1"

def test_case_7():
    input = [5]
    output = solution(input)
    assert output == "5"

def test_case_8():
    input = [-1]
    output = solution(input)
    assert output == "-1"

def test_case_9():
    input = [-5]
    output = solution(input)
    assert output == "-5"

def test_case_10():
    input = [-5, -2]
    output = solution(input)
    assert output == "10"

def test_case_11():
    input = [-55, 66]
    output = solution(input)
    assert output == "66"

def test_case_12():
    input = [55, -66]
    output = solution(input)
    assert output == "55"

def test_case_14():
    input = [66, -55]
    output = solution(input)
    assert output == "66"

def test_case_15():
    input = [-66, 55]
    output = solution(input)
    assert output == "55"

def test_case_16():
    input = [5, 6]
    output = solution(input)
    assert output == "30"

def test_case_17():
    input = [0, 1]
    output = solution(input)
    assert output == "1"

def test_case_18():
    input = [1, 0]
    output = solution(input)
    assert output == "1"

def test_case_19():
    input = [0, 55]
    output = solution(input)
    assert output == "55"

def test_case_20():
    input = [55, 0]
    output = solution(input)
    assert output == "55"

def test_case_21():
    input = [0, -1]
    output = solution(input)
    assert output == "0"

def test_case_22():
    input = [-1, 0]
    output = solution(input)
    assert output == "0"

def test_case_23():
    input = [0, -66]
    output = solution(input)
    assert output == "0"

def test_case_24():
    input = [-66, 0]
    output = solution(input)
    assert output == "0"

def test_case_25():
    input = [0, 77]
    output = solution(input)
    assert output == "77"

def test_case_26():
    input = [77, 0]
    output = solution(input)
    assert output == "77"

def test_case_27():
    input = [0, 5, 5]
    output = solution(input)
    assert output == "25"

def test_case_28():
    input = [5, 0, 5]
    output = solution(input)
    assert output == "25"

def test_case_29():
    input = [5, 5, 0]
    output = solution(input)
    assert output == "25"

def test_case_30():
    input = [0, 5, -6]
    output = solution(input)
    assert output == "5"

def test_case_31():
    input = [5, 0, -6]
    output = solution(input)
    assert output == "5"

def test_case_32():
    input = [5, -6, 0]
    output = solution(input)
    assert output == "5"

def test_case_33():
    input = [-6, 5, 0]
    output = solution(input)
    assert output == "5"

def test_case_34():
    input = [0, -3, -4]
    output = solution(input)
    assert output == "12"

def test_case_35():
    input = [-3, 0, -4]
    output = solution(input)
    assert output == "12"

def test_case_36():
    input = [-3, -4, 0]
    output = solution(input)
    assert output == "12"

def test_case_37():
    input = [-4, -3, 0]
    output = solution(input)
    assert output == "12"

def test_case_38():
    input = [0, 1, 5]
    output = solution(input)
    assert output == "5"

def test_case_39():
    input = [1, 0, 5]
    output = solution(input)
    assert output == "5"

def test_case_40():
    input = [1, 5, 0]
    output = solution(input)
    assert output == "5"

def test_case_41():
    input = [5, 1, 0]
    output = solution(input)
    assert output == "5"

def test_case_42():
    input = [1, -4, -6]
    output = solution(input)
    assert output == "24"

def test_case_43():
    input = [-4, 1, -6]
    output = solution(input)
    assert output == "24"

def test_case_44():
    input = [-4, -6, 1]
    output = solution(input)
    assert output == "24"

def test_case_45():
    input = [-6, -4, 1]
    output = solution(input)
    assert output == "24"

def test_case_46():
    input = [-6, 1, -4]
    output = solution(input)
    assert output == "24"

def test_case_47():
    input = [1, 1, 0]
    output = solution(input)
    assert output == "1"

def test_case_48():
    input = [1, 0, 1]
    output = solution(input)
    assert output == "1"

def test_case_49():
    input = [0, 1, 1]
    output = solution(input)
    assert output == "1"

def test_case_50():
    input = [1, 1, 1, 1, 45]
    output = solution(input)
    assert output == "45"

def test_case_51():
    input = [0, 0, 0, 68, 0, 0, 0]
    output = solution(input)
    assert output == "68"

def test_case_52():
    input = [2, 3, 2, 2]
    output = solution(input)
    assert output == "24"

def test_case_53():
    input = [-2, -2, -3]
    output = solution(input)
    assert output == "6"

def test_case_54():
    input = [-2, -2, -2, -3]
    output = solution(input)
    assert output == "24"

def test_case_55():
    input = [-2, -2, 0, 0, -2, -3]
    output = solution(input)
    assert output == "24"

def test_case_56():
    input = [2, 3, 0, 0, 2, 2]
    output = solution(input)
    assert output == "24"

def test_case_57():
    input = [-2, -2, 0, 0, 2, 3]
    output = solution(input)
    assert output == "24"

def test_case_58():
    input = [0, 0]
    output = solution(input)
    assert output == "0"

# def test_case_59():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_60():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_61():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_62():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_63():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_64():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_65():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_66():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_67():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_68():
#     input = []
#     output = solution(input)
#     assert output == ""
#
# def test_case_69():
#     input = []
#     output = solution(input)
#     assert output == ""
