
import json
import argparse
import copy


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creates excellence")

    # create arguments
    parser.add_argument('-x', action="store", help="Name of the noob")

    # actualy parse the args and create the namespace
    args_namespace = parser.parse_args()

    print(args_namespace, end="\n\n")

    # make a hard clone
    args_dict = copy.deepcopy(args_namespace.__dict__)

    # remove the none values
    result = dict(
        filter(
            lambda elem: elem[1] != None,
            args_dict.items()
        )
    )

    print(result)
