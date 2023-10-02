import os
import pathlib

from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree

IGNORED_DIRS = (".git", ".venv", "__pycache__", "node_modules")
IGNORED_FILES = (".DS_Store", ".gitignore", ".python-version", 
                 "__init__.py", "__main__.py")
IGNORE_FILETYPES = (".ignore")

def format_tree_dir(dir_path: pathlib.Path, is_last_depth: bool) -> Text:
    """Return a formatted Text directory path to go to the Tree."""
    contents = os.listdir(dir_path)

    style = "dim" if (dir_path.name.startswith(".") or 
                      dir_path.name.startswith("__") or
                      len(contents) == 0) else ""
    text_str = f"[bold cyan]:open_file_folder: [link file://{dir_path}]{escape(dir_path.name)}"

    # Add '...' if is_last_depth and the directory contains a file
    if is_last_depth:
        if len(contents) > 0:
            text_str += "..."

    text = Text(
        text=text_str,
        style=style,
        guide_style=style,
        overflow="ellipsis",
        max_length=30,
    )
    return text

def format_tree_file(file_path: pathlib.Path) -> Text:
    """Return a formatted Text file path to go to the Tree."""
    file_size = decimal(file_path.stat().st_size)
    icon = "🐍 " if file_path.suffix == ".py" else "📄 "

    style = "dim" if (file_path.name.startswith(".") or 
                      file_path.name.startswith("__")) else ""
    
    text_filename = Text(text=f"{icon} [green]{file_path.name}", style=style)
    # text_filename.stylize("dim", len(file_path.suffix))
    text_filename.highlight_regex(r"\.(py|js|html|css|md|txt|json|yml|yaml|toml|c|lmp|cpp|v)$", 
                                  "bold")
    text_filename.stylize(f"link file://{file_path}")
    text_filename.append(f" ({file_size})", "blue")

    return text_filename

def walk_dir(directory: pathlib.Path, tree: Tree, 
             ignore_files: bool, ignore_dirs: bool, ignore_filetypes: bool,
             search_depth: int, maximum_depth: int = 3):
    """Walk a directory and add its contents to a tree."""
    
    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )

    for path in paths:
        # Skip hidden files
        if path.name.startswith("."):
            continue

        # Skip ignored directories
        if path.is_dir() and ignore_dirs and path.name in IGNORED_DIRS:
            continue

        # Skip ignored files
        if path.is_file() and ignore_files and path.name in IGNORED_FILES:
            continue

        # Skip ignored filetypes
        if path.is_file() and ignore_filetypes and path.suffix in IGNORE_FILETYPES:
            continue

        # Do smth if path is a directory
        if path.is_dir():
            if search_depth < maximum_depth:
                child = tree.add(format_tree_dir(path, is_last_depth=False))
                walk_dir(path, child, ignore_files, ignore_dirs, ignore_filetypes,
                         search_depth + 1, maximum_depth)
            else:
                tree.add(format_tree_dir(path, is_last_depth=True))
        # Do smth if path is a file
        else:
            tree.add(format_tree_file(path))
