from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    """
    Extrai texto de um PDF carregado via Streamlit.

    Parameters:
    - pdf_file (UploadedFile): Arquivo PDF enviado.

    Returns:
    - str: Texto extraído do PDF.
    """
    reader = PdfReader(pdf_file)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text
