from util.get_first_unique_element import get_first_unique_element


def get_fist_unique_for_words(text: str) -> str | None:
    if not isinstance(text, str):
        raise TypeError(
            f"the 'text' argument must be a str-type, but  got type {type(text)}"
        )
    firsts_for_words_list = [get_first_unique_element(elem) for elem in text.split()]
    return get_first_unique_element(firsts_for_words_list)


if __name__ == "__main__":
    cases = [
        (
            """
        The Tao gave birth to machine language.  Machine language gave birth to the assembler.
        The assembler gave birth to the compiler.  Now there are ten thousand languages.
        Each language has its purpose, however humble.  Each language expresses the Yin and Yang
        of software.  Each language has its place within the Tao.
        But do not program in COBOL if you can avoid it.
            -- Geoffrey James, "The Tao of Programming"
        """,
            "m",
        ),
    ]
    for case in cases:
        assert (
            get_fist_unique_for_words(case[0]) == case[1]
        ), f"test falled: get_first_unique_element({case[0]}) == {case[1]}"
    print("all tests passed")
