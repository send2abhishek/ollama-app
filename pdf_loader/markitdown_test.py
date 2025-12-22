import warnings
from markitdown import MarkItDown
from pathlib import Path
import os


warnings.filterwarnings("ignore")

os.makedirs('markitdown', exist_ok=True)





md = MarkItDown()
file_path = Path("doc/onbord.pdf")

print(file_path.stem)

result = md.convert(file_path)

# print(result.text_content[:500])

with open(f"markitdown/{file_path.stem}.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)
