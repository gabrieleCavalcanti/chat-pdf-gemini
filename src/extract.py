# from pypdf import PdfReader


# def extract_text_from_pdf(pdf_file):
#     """
#     Função para extrair o texto de um pdf carregado o Streamlit.

#     Parâmetros:
#     pdf_file(UploadedFile)

#     retorno:
#     src: texto extraído do PDF.

#     """
#     reader = PdfReader(pdf_file)

#     # reader = pypdf.Pdfreader(pdf_file) #Cria um objeto para ler o PDF

#     # Percorrer todas as páginas e extrair informações
#     text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

#     return text # retorna o texto extraído




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
