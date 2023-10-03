import argparse
from rich.console import Console

from . import utils
from . import force_fields

def main():
    parser = argparse.ArgumentParser(
        description="Plot potentials.",
        prog="fields",
        epilog="Created by Pedro Juan Royo @UnstrayCato"
    )
    parser.set_defaults(which="main")

    parser.add_argument(
        "--version", "-v", action="version", version="%(prog)s v0.17.0"
    )

    available_fields = [a.value for a in utils.Fields]
    parser.add_argument(
        "--field", "-f", nargs="*", choices=available_fields,
        help="Force field to plot"
    )

    args = parser.parse_args()
    print(args)

    console = Console()
    if args.which == "main":
        with console.status("[bold green]Plot created"):
            force_fields.plot_field(points = utils.create_range(0.9,3,60),
                                    epsilon = 1, sigma = 1.0, cut = 3.5)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()