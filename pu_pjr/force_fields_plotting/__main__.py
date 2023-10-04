import argparse
from rich.console import Console
from rich.text import Text

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

    subparsers = parser.add_subparsers(title="subcommands", dest="which")
    list_parser = subparsers.add_parser(
        "list", help="list available force fields"
    )
    list_parser.set_defaults(which="list")

    plot_parser = subparsers.add_parser(
        "show", help="plot a force field"
    )
    plot_parser.set_defaults(which="main")

    plot_parser.add_argument(
        "--y-range", "-y", type=float, nargs=2, default=[-5.0, 10.0],
        help = "Min value for range in plot points, default 0.9"
    )
    plot_parser.add_argument(
        "--range-min", "-r", type=float, default=0.9,
        #metavar="kwargs",
        help = "Min value for range in plot points, default 0.9"
    )
    plot_parser.add_argument(
        "--range-max", "-R", type=float, default=3.0,
        #metavar="kwargs",
        help = "Min value for range in plot points, default 3.0"
    )
    plot_parser.add_argument(
        "--range-points", "-p", type=int, default=30,
        #metavar="kwargs",
        help = "Number of points in range, default 30"
    )
    plot_parser.add_argument(
        "--line-type", "-l", type=str, default="o-",
        #metavar="kwargs",
        help = "Line type for plot, default 'o-'"
    )
    plot_parser.add_argument(
        "potential_data", nargs="+",
        #metavar="kwargs",
        help = "Force field data to plot POTENTIAL must be a valid field name and DATA"+
            "must be valid keyword arguments for the potential."
    )

    args = parser.parse_args()
    # print(args)

    console = Console()
    if args.which == "main":
        keyargpairs = utils.parse_keyargpairs(args.potential_data)
        # print(keyargpairs)

        with console.status("[bold green]Plot created"):
            # force_fields.plot_field(points = utils.create_range(0.9,3,60),
            #                         epsilon = 1.0, sigma = 1.0, cut = 3.5)
            for field in keyargpairs:
                points = utils.create_range(args.range_min, 
                                            args.range_max, 
                                            args.range_points)
                force_fields.plot_field(utils.Potentials[utils.remove_extras_for_class(field)], 
                                        points, 
                                        args.line_type,
                                        args.y_range,
                                        **keyargpairs[field])
    elif args.which == "list":
        descriptions, max_length = utils.field_descriptions()
        for field in descriptions:
            text = Text(f"{field.replace('/', '_'):>{max_length}}: "
                        f"{descriptions[field]}")
            text.stylize("bold green", 0, max_length)
            text.stylize("bold blue", max_length + 2, len(text))
            text.highlight_regex("ARGS:.*", "bold yellow")
            console.print(text)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()