from rich.table import Table
from rich import box
import os

from . import utils

def get_dir_contents(path: str = './', ignore_hidden: bool = True) -> Table:
    """Get the contents of a directory.

    Args:
        path (str): Path to the directory.

    Returns:
        list: List of files and directories in the directory.
    """
    files, dirs = utils.get_dir_files(path, include_dirs=True)
    
    file_sizes = []
    for file in files:
        file_sizes.append(utils.get_file_size(os.path.join(path, file)))

    table = Table(#title="Directory contents", 
                  show_header=True, header_style="bold",
                  show_lines=True, padding=(0,2), box=box.SIMPLE, 
                  highlight=True, footer_style="bold", show_footer=True)

    table.add_column(header="Name")
    # table.add_column(header="Type")
    table.add_column(header="Size", justify="right", style="cyan")

    for pos,file in enumerate(files):
        table.add_row(file, str(file_sizes[pos]))

    # Add footer to table
    table.add_row("Total", str(sum(file_sizes)))
        
    return table
