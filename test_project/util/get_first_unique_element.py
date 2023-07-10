from collections.abc import Sequence
from typing import TypeVar

Type_of_inside_element = TypeVar("Type_of_inside_element")


def get_first_unique_element(
    seq: Sequence[Type_of_inside_element],
) -> Type_of_inside_element | None:
    """For a sequence, returns the first element that does not occur in the remainder of the sequence.

    >>> seq_str = "abcdea"
    >>> get_first_unique_element(seq_str)
    'b'
    >>> get_first_unique_element(["aa", None, True, None, "aa"])
    True

    If the passed value is not a sequence, an exception TypeError is raised:
    >>> get_first_unique_element(11)
    Traceback (most recent call last):
    ...
    TypeError: the 'seq' argument must be a sequence, but  got type <class 'int'>
    """
    if not isinstance(seq, Sequence):
        raise TypeError(
            f"the 'seq' argument must be a sequence, but  got type {type(seq)}"
        )
    for index, element in enumerate(seq):
        if element not in seq[index + 1 :]:
            return element


if __name__ == "__main__":
    cases = [
        ("asdf", "a"),
        ("bbbaaa", "b"),
        (["one", "two", "one"], "two"),
        ((None, True, 22), None),
    ]

    for case in cases:
        assert (
            get_first_unique_element(case[0]) == case[1]
        ), f"test falled: get_first_unique_element({case[0]}) == {case[1]}"
    print("all tests passed")
