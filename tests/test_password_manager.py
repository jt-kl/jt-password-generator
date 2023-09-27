import pytest

from jt_password_generator.managers import PasswordManager, SeedManager

# region: pytest parametrized variables
generate_password_happy = [
    (
        {
            "seed_manager": {
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
            "length": 8,
            "count": 10,
        },
        {"length": 8, "count": 10},
    ),
]

generate_entropy_happy = [
    (
        {
            "seed_manager": {
                "lowers": True,
                "uppers": True,
                "numbers": False,
                "logograms": False,
                "punctuations": False,
                "quotes": False,
                "dashes": False,
                "slashes": False,
                "operators": False,
                "braces": False,
                "inclusions": "",
                "exclusions": "",
            },
            "length": 12,
            "count": 2,
        },
        {
            "entropy": 68.4052766176931,
        },
    ),
]
# endregion: pytest parametrized variables


class TestPasswordManagerMethods:
    @pytest.mark.parametrize("payload, expect", generate_password_happy)
    def test_generate_password(self, payload, expect):
        seed_manager = SeedManager(**payload.pop("seed_manager"))
        password_manager = PasswordManager(seed_manager, **payload)

        collection = password_manager.generate_password()

        assert expect["count"] == len(collection)

        for i in collection:
            assert expect["length"] == len(i["password"])
            assert "encoded" in i.keys()
            assert "entropy" in i.keys()

    @pytest.mark.parametrize("payload, expect", generate_entropy_happy)
    def test_generate_entropy(self, payload, expect):
        seed_manager = SeedManager(**payload.pop("seed_manager"))
        password_manager = PasswordManager(seed_manager, **payload)

        entropy = password_manager._generate_entropy()

        assert expect["entropy"] == entropy
