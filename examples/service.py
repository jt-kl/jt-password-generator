from argparse import ArgumentParser
from os import system
from pprint import PrettyPrinter

from jt_password_generator.managers import PasswordManager, SeedManager

# region: Global variables
# endregion: Global variables


def validate_options(options):
    """
    Validate Argument Options

    Args:
        options: ArgumentParser option
    """
    seeds = [
        options.lowers,
        options.uppers,
        options.numbers,
        options.logograms,
        options.punctuations,
        options.quotes,
        options.dashes,
        options.slashes,
        options.operators,
        options.braces,
    ]

    if not any(seeds):
        raise ValueError(
            (
                "At least one seed character option must be specified. "
                "Specify any of the following seeds: lowers, uppers, "
                "numbers, logograms, punctuations, quotes, dashes, slashes, "
                "operators or braces"
            )
        )


def main(options):
    """
    Password Generator

    Args:
        options: ArgumentParser option
    """
    # TODO Add unit testing
    # TODO Add GitHub action workflows
    # TODO Add profile setup options
    # TODO Add profile remove options
    # TODO Add profile call options

    system("clear")

    validate_options(options)

    seed_manager = SeedManager(
        options.lowers,
        options.uppers,
        options.numbers,
        options.logograms,
        options.punctuations,
        options.quotes,
        options.dashes,
        options.slashes,
        options.operators,
        options.braces,
        inclusions=options.inclusions,
        exclusions=options.exclusions,
    )
    password_manager = PasswordManager(seed_manager)
    passwords = password_manager.generate_password()

    pp = PrettyPrinter(indent=2, sort_dicts=False)
    pp.pprint(passwords)


if __name__ == "__main__":
    p = ArgumentParser(description="Generate Password")
    p.add_argument("--lowers", help="Include lowercase", action="store_true", default=True)
    p.add_argument("--uppers", help="Include uppercase", action="store_true")
    p.add_argument("--numbers", help="Include numbers", action="store_true")
    p.add_argument("--logograms", help="Include logograms", action="store_true")
    p.add_argument("--punctuations", help="Include punctuations", action="store_true")
    p.add_argument("--quotes", help="Include quotes", action="store_true")
    p.add_argument("--dashes", help="Include dashes", action="store_true")
    p.add_argument("--slashes", help="Include slashes", action="store_true")
    p.add_argument("--operators", help="Include operators", action="store_true")
    p.add_argument("--braces", help="Include braces", action="store_true")
    p.add_argument(
        "--inclusions",
        help='Characters to include in seed (Example: "24cs!")',
        default="",
    )
    p.add_argument(
        "--exclusions",
        help='Characters to exclude from seed (Example: "gdk^")',
        default="",
    )
    p.add_argument(
        "--length",
        help="Password length (Default: 16 characters)",
        type=int,
        default=16,
    )
    p.add_argument("--count", help="Password count (Default: 10 passwords)", type=int, default=5)

    options = p.parse_args()

    main(options)
    main(options)
