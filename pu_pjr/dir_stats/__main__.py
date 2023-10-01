import argparse
from rich.console import Console

# from . import utils
from . import dir_contents

def main():
    # console = Console()

    # console.print("Hello", "World", ":smile:", 
    #               style="bold red")
    
    # table = Table(title="Table title")

    # table.add_column(header="Test")
    # table.add_column(header="Content", )

    # table.add_row("Item 1")

    # console.print(table)

    table = dir_contents.get_dir_contents()
    console = Console()
    
    with console.pager():
        console.print(table)
    

if __name__ == "__main__":
    main()