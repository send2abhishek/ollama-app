from docling.document_converter import DocumentConverter
import os
from pathlib import Path

os.makedirs('docling/tables', exist_ok=True)

converter = DocumentConverter()

# filename = "doc/onbord.pdf"




def convert_and_save(filename):
    filepath = Path(filename)
    print(filepath)
    result = converter.convert(filepath)
    print(result.document.tables)
    for i,table in enumerate(result.document.tables):
        df = table.to_dataframe()
        df.to_csv(f'docling/tables/{filepath.stem}_table_{i+1}.csv', index=False)
    # markdown_result = result.document.export_to_markdown()
    # with open(f"docling/{filepath.stem}.md", "w", encoding="utf-8") as f:
    #     f.write(markdown_result)


convert_and_save("doc/apple.pdf")