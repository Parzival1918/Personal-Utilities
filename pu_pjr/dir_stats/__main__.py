import argparse
from rich.console import Console

# from . import utils
from . import dir_contents

def main():
    parser = argparse.ArgumentParser(
        description="Get information about directory contents.",
        prog="dirstats",
        epilog="Created by Pedro Juan Royo @UnstrayCato"
    )

    parser.add_argument(
        "--version", "-v", action="version", version="%(prog)s v0.10.0"
    )

    # Sub-parser for the "tree" command
    subparser = parser.add_subparsers()
    tree_parser = subparser.add_parser(
        "tree", help="Get a tree of the directory contents",
        epilog="Created by Pedro Juan Royo @UnstrayCato"
    )
    tree_parser.set_defaults(which="tree")

    tree_parser.add_argument(
        "--directory", "-D", type=str, default="./",
        help="The directory to get the contents of"
    )
    tree_parser.add_argument(
        "--depth", "-d", type=int, default=2,
        help="The maximum depth to search for files and folders. Default is 2"
    )
    tree_parser.add_argument(
        "--pager", "-p", action="store_true",
        help="Show the output in a pager"
    )
    # console = Console()

    # console.print("Hello", "World", ":smile:", 
    #               style="bold red")
    
    # table = Table(title="Table title")

    # table.add_column(header="Test")
    # table.add_column(header="Content", )

    # table.add_row("Item 1")

    # console.print(table)

    # table = dir_contents.get_dir_contents()
    # console = Console()
    
    # with console.pager():
    #     console.print(table)

    args = parser.parse_args()

    if args.which == "tree":
        tree = dir_contents.get_dir_contents(dir=args.directory, maximum_depth=args.depth)
        console = Console()
        if args.pager:
            with console.pager():
                console.print(tree)
        else:
            console.print(tree)

if __name__ == "__main__":
    main()