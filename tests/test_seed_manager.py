from string import ascii_lowercase, ascii_uppercase, digits

import pytest

from jt_password_generator.managers import SeedManager

# region: pytest parametrized variables
generate_seed_happy = [
    (
        {
            "lowers": True,
            "uppers": True,
            "numbers": True,
            "logograms": True,
            "punctuations": True,
            "quotes": True,
            "dashes": True,
            "slashes": True,
            "operators": True,
            "braces": True,
            "inclusions": "",
            "exclusions": "",
        },
        {
            "characters": [
                *list(ascii_lowercase),
                *list(ascii_uppercase),
                *list(digits),
                *["#", "$", "%", "&", "@", "^", "`", "~"],
                *[".", ",", ":", ";"],
                *['"', "'"],
                *["_", "-"],
                *["\\", "/", "|"],
                *["<", ">", "*", "+", "!", "?", "="],
                *["{", "}", "[", "]", "(", ")"],
            ],
        },
    ),
    (
        {
            "lowers": True,
            "uppers": True,
            "numbers": False,
            "logograms": True,
            "punctuations": True,
            "quotes": True,
            "dashes": True,
            "slashes": True,
            "operators": True,
            "braces": True,
            "inclusions": "123",
            "exclusions": "_|",
        },
        {
            "characters": [
                *list(ascii_lowercase),
                *list(ascii_uppercase),
                *["#", "$", "%", "&", "@", "^", "`", "~"],
                *[".", ",", ":", ";"],
                *['"', "'"],
                *["-"],
                *["\\", "/"],
                *["<", ">", "*", "+", "!", "?", "="],
                *["{", "}", "[", "]", "(", ")"],
            ],
        },
    ),
]
# endregion: pytest parametrized variables


class TestSeedManagerMethods:
    @pytest.mark.parametrize("payload, expect", generate_seed_happy)
    def test_generate_seed(self, payload, expect):
        manager = SeedManager(**payload)

        for c in expect["characters"]:
            assert c in manager.generate_seed()


class TestSeedManagerClass:
    def test_class_attributes(self):
        assert hasattr(SeedManager, "SEQUENCE_BRACES")
        assert hasattr(SeedManager, "SEQUENCE_DASHES")
        assert hasattr(SeedManager, "SEQUENCE_LOGOGRAMS")
        assert hasattr(SeedManager, "SEQUENCE_LOWERCASES")
        assert hasattr(SeedManager, "SEQUENCE_NUMBERS")
        assert hasattr(SeedManager, "SEQUENCE_OPERATORS")
        assert hasattr(SeedManager, "SEQUENCE_PUNCTUATIONS")
        assert hasattr(SeedManager, "SEQUENCE_QUOTES")
        assert hasattr(SeedManager, "SEQUENCE_SLASHES")
        assert hasattr(SeedManager, "SEQUENCE_UPPERCASES")

    def test_class_attribute_contents(self):
        for c in ["{", "}", "[", "]", "(", ")"]:
            assert c in SeedManager.SEQUENCE_BRACES

        for c in ["_", "-"]:
            assert c in SeedManager.SEQUENCE_DASHES

        for c in ["#", "$", "%", "&", "@", "^", "`", "~"]:
            assert c in SeedManager.SEQUENCE_LOGOGRAMS

        for c in list(ascii_lowercase):
            assert c in SeedManager.SEQUENCE_LOWERCASES

        for c in list(digits):
            assert c in SeedManager.SEQUENCE_NUMBERS

        for c in ["<", ">", "*", "+", "!", "?", "="]:
            assert c in SeedManager.SEQUENCE_OPERATORS

        for c in [".", ",", ":", ";"]:
            assert c in SeedManager.SEQUENCE_PUNCTUATIONS

        for c in ['"', "'"]:
            assert c in SeedManager.SEQUENCE_QUOTES

        for c in ["\\", "/", "|"]:
            assert c in SeedManager.SEQUENCE_SLASHES

        for c in list(ascii_uppercase):
            assert c in SeedManager.SEQUENCE_UPPERCASES
