# convert_pdf.py
from pdf2image import convert_from_path
import pathlib

def pdf_to_images(pdf_path: str, out_dir: str = "/app/data/pages", dpi: int = 300):
    pdf = pathlib.Path(pdf_path)
    pages = convert_from_path(pdf, dpi=dpi)
    out = pathlib.Path(out_dir)
    out.mkdir(exist_ok=True)
    for i, page in enumerate(pages, 1):
        img_path = out / f"{pdf.stem}_{i:03}.png"
        page.save(img_path, "PNG")
        yield img_path

if __name__ == "__main__":
    import sys
    for p in pdf_to_images(sys.argv[1]):
        print(p)