from pypdf import PdfWriter

merger = PdfWriter()

for pdf in [r"L76_SP\Aam.pdf" , r"L76_SP\Chappal.pdf"]:
    merger.append(pdf)

merger.write(r"L76_SP\merged.pdf")