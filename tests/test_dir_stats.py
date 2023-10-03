from pu_pjr.dir_stats import utils

from rich.text import Text
import pathlib

def test_folder_emoji():
    assert utils.folder_emoji(pathlib.Path.cwd()) == "📂"
    assert utils.folder_emoji(pathlib.Path.cwd() / "tests") == "📂"

def test_format_tree_dir():
    assert utils.format_tree_dir(pathlib.Path.cwd(), False) == \
            Text("📂 Personal-Utilities", style="cyan")
    assert utils.format_tree_dir(pathlib.Path.cwd(), True) == \
            Text("📂 Personal-Utilities (...)", style="cyan")
    assert utils.format_tree_dir(pathlib.Path.cwd() / ".github", True) == \
            Text("📂 .github (...)", style="dim cyan")
    
def test_file_emoji():
    assert utils.file_emoji(pathlib.Path.cwd() / "README.md") == "📝"
    assert utils.file_emoji(pathlib.Path.cwd() / "tests" / "test_dir_stats.py") == "🐍"

def test_format_tree_file():
    assert utils.format_tree_file(pathlib.Path.cwd() / "README.md")._text[0] == \
            Text("📝 README.md", style="green")._text[0]
    assert utils.format_tree_file(pathlib.Path.cwd() / "tests" / 
            "test_dir_stats.py")._text[0] == \
            Text("🐍 test_dir_stats.py", style="green")._text[0]
    assert utils.format_tree_file(pathlib.Path.cwd() / "wrong.txt")._text[0] == \
            Text("⛔️ wrong.txt", style="green")._text[0]