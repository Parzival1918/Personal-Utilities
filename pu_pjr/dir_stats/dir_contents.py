from rich.tree import Tree
import pathlib

from . import utils

def get_dir_contents(dir: pathlib.Path = pathlib.Path.cwd(), 
                     maximum_depth: int = 3) -> Tree:
    """Return a Tree containing the contents of a directory."""
    tree = Tree(
        # f":open_file_folder: [link file://{dir}]{dir}",
        f":open_file_folder: {dir}",
    )

    utils.walk_dir(dir, tree, ignore_files=False, ignore_dirs=False,
                   ignore_filetypes=False, search_depth=0, maximum_depth=maximum_depth)

    return tree