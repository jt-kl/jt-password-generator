import math
import secrets
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Any
from urllib.parse import quote

# region: Global variables
# endregion: Global variables


class SeedManager:
    SEQUENCE_BRACES = ["{", "}", "[", "]", "(", ")"]
    SEQUENCE_DASHES = ["_", "-"]
    SEQUENCE_LOGOGRAMS = ["#", "$", "%", "&", "@", "^", "`", "~"]
    SEQUENCE_LOWERCASES = list(ascii_lowercase)
    SEQUENCE_NUMBERS = list(digits)
    SEQUENCE_OPERATORS = ["<", ">", "*", "+", "!", "?", "="]
    SEQUENCE_PUNCTUATIONS = [".", ",", ":", ";"]
    SEQUENCE_QUOTES = ['"', "'"]
    SEQUENCE_SLASHES = ["\\", "/", "|"]
    SEQUENCE_UPPERCASES = list(ascii_uppercase)

    def __init__(
        self,
        lowers: bool,
        uppers: bool,
        numbers: bool,
        logograms: bool,
        punctuations: bool,
        quotes: bool,
        dashes: bool,
        slashes: bool,
        operators: bool,
        braces: bool,
        inclusions: str,
        exclusions: str,
    ):
        """
        Constructor

        Args:
            lowers: Include lowercase characters
            uppers: Include uppercase characters
            numbers: Include numbers
            logograms: Include logograms
            punctuations: Include
            quotes: Include quotes
            dashes: Include dashes
            slashes: Include slashes
            operators: Include operators
            braces: Include braces
            inclusions: List of characters to include
            exclusions: List of characters to exclude
        """
        self.lowers = lowers
        self.uppers = uppers
        self.numbers = numbers
        self.logograms = logograms
        self.punctuations = punctuations
        self.quotes = quotes
        self.dashes = dashes
        self.slashes = slashes
        self.operators = operators
        self.braces = braces
        self.inclusions = list(inclusions)
        self.exclusions = list(exclusions)

    def generate_seed(self) -> set[str]:
        """
        Generate Character Seeds
        """
        seeds = list()

        if self.lowers:
            seeds.extend(self.SEQUENCE_LOWERCASES)

        if self.uppers:
            seeds.extend(self.SEQUENCE_UPPERCASES)

        if self.numbers:
            seeds.extend(self.SEQUENCE_NUMBERS)

        if self.logograms:
            seeds.extend(self.SEQUENCE_LOGOGRAMS)

        if self.punctuations:
            seeds.extend(self.SEQUENCE_PUNCTUATIONS)

        if self.quotes:
            seeds.extend(self.SEQUENCE_QUOTES)

        if self.dashes:
            seeds.extend(self.SEQUENCE_DASHES)

        if self.slashes:
            seeds.extend(self.SEQUENCE_SLASHES)

        if self.operators:
            seeds.extend(self.SEQUENCE_OPERATORS)

        if self.braces:
            seeds.extend(self.SEQUENCE_BRACES)

        for i in self.inclusions:
            if i not in seeds:
                seeds.append(i)

        # ? Exclusion parameter takes precedence over inclusion parameters
        for i in self.exclusions:
            if i in seeds:
                seeds.remove(i)

        return set(seeds)


class PasswordManager:
    def __init__(
        self,
        seed_manager: SeedManager,
        length: int = 16,
        count: int = 10,
    ):
        """
        Constructor

        Args:
            seed: Character seed instance
            length: Minimum password length
            count: Number of password to generate
        """
        self.seed_manager = seed_manager
        self.length = length
        self.count = count

    def _generate_entropy(self) -> float:
        """
        Generate Password Entropy
        """
        # ? Formula: E = log2 (R**L)
        # ? Where E = Entropy result in bits
        # ? Where R = Size of the pool of unique characters
        # ? Where L = Length of password
        entropy = math.log2(len(self.seed_manager.generate_seed()) ** self.length)

        return entropy

    def generate_password(self) -> list[dict[str, str | Any]]:
        """
        Generate Password
        """
        collection = list()

        for _ in range(self.count):
            seeds = self.seed_manager.generate_seed()
            password = "".join([secrets.choice(list(seeds)) for _ in range(self.length)])
            encoded = quote(password)
            entropy = self._generate_entropy()

            collection.append(
                {
                    "password": password,  # Regular password
                    "encoded": encoded,  # URL encoded password
                    "entropy": entropy,  # Value in bits
                }
            )

        return collection
