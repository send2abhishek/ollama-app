import warnings
from markitdown import MarkItDown
from pathlib import Path
import os


warnings.filterwarnings("ignore")

os.makedirs('markitdown', exist_ok=True)





md = MarkItDown()

def convert_save(file_path):
    file_path = Path(file_path)
    result = md.convert(file_path)

    with open(f"markitdown/{file_path.stem}.md", "w", encoding="utf-8") as f:
        f.write(result.text_content)


convert_save("doc/onbord.pdf")
