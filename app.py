from flask import Flask, request
import PyPDF2

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Assesment for Vaultedge Software Private Limited"


@app.route('/rotate-pdf', methods=['POST'])
def rotate_pdf():
    request_data = request.get_json()
    file_path = request_data["file_path"]
    angle_of_rotation = int(request_data["angle_of_rotation"])
    page_number = int(request_data['page_number'])
    pdf_reader = PyPDF2.PdfFileReader(file_path, strict=False)
    pdf_writer = PyPDF2.PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum == page_number:
            page.rotateClockwise(angle_of_rotation)
        pdf_writer.addPage(page)
    with open(file_path, "wb") as file:
        pdf_writer.write(file)
    return request_data


app.run(debug=True)
