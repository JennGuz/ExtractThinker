import os

from pydantic import BaseModel, Field
from dotenv import load_dotenv

from extract_thinker import DocumentLoaderTesseract, Extractor

load_dotenv()
cwd = os.getcwd()

class InvoiceContract(BaseModel):
    invoice_number: str = Field(..., description="Número de la factura")
    invoice_date: str = Field(..., description="Fecha de emisión de la factura")
    destinatary: str = Field(..., description="Destinatario de la factura")
    summary: str = Field(..., description="Resumen de la factura con al menos de 200 caracteres")


tesseract_path = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

test_file_path = os.path.join(cwd, "tests", "test_images", "invoice.png")

print("Iniciando programa")
extractor = Extractor()
extractor.load_document_loader(
    DocumentLoaderTesseract(tesseract_path)
)
extractor.load_llm("gpt-4.1-mini")

result = extractor.extract(test_file_path, InvoiceContract)

if result is not None:
    print("Extraction successful.")
else:
    print("Extraction failed.")

print("Invoice Number: ", result.invoice_number)
print("Invoice Date: ", result.invoice_date)
print("Invoice Destinatary", result.destinatary)
print("Summary", result.summary)
