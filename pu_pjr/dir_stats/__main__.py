import argparse
from rich.console import Console
from rich.table import Table

from . import utils

def main():
    console = Console()

    console.print("Hello", "World", ":smile:", 
                  style="bold red")
    
    table = Table(title="Table title")

    table.add_column(header="Test")
    table.add_column(header="Content", )

    table.add_row("Item 1")

    console.print(table)
    

if __name__ == "__main__":
    main()