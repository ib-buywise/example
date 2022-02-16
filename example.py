from typing import List


class SomeMethod:
    def __init__(self) -> None:
        pass

    def above_below(self, unsorted_int_list: List[int], checked_int: int) -> dict:
        return_dict = {"above": 0, "below": 0}

        for unsorted_int in unsorted_int_list:
            if unsorted_int == checked_int:
                continue
            return_dict.update({"above": return_dict["above"] + 1} if unsorted_int > checked_int else {"below": return_dict["below"] + 1})

        return return_dict


def run_tests():

    some_method_object = SomeMethod()
    assert isinstance(some_method_object, SomeMethod)

    test_integers = [1, 2, 3, 4, 5, 6, 7]
    test_integer_target = 6

    result_dict = some_method_object.above_below(test_integers, test_integer_target)
    print(result_dict)


if __name__ == "__main__":
    run_tests()
