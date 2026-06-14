from pypdf import PdfReader


def load_pdfs(files):

    text=""

    for file in files[:30]:

        pdf=PdfReader(file)

        for page in pdf.pages:
            text+=page.extract_text()

    return text
