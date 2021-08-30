from flask.helpers import find_package
from config import *
from model import FileContents

@app.route('/')
def index():
    files = FileContents.query.all()
    
    return render_template('index.html', files = files)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']

    picFile = request.files['picFile']


    if file.filename != '':
        formato = file.filename.split('.')[-1]
        nome = file.filename.split('.')[0]
        novoArquivo = FileContents(name=nome, formato=formato, data=file.read())
        db.session.add(novoArquivo)
        db.session.commit()
    else:
        formato = picFile.filename.split('.')[-1]
        nome = picFile.filename.split('.')[0]
        novoArquivo = FileContents(name=nome, formato=formato, data=picFile.read())
        db.session.add(novoArquivo)
        db.session.commit()


    return 'Arquivo: ' + nome + ' com a extensão: ' + formato + ' salvo no banco de dados.' + '<br><a href="/">Voltar</a>' 


@app.route('/download/<int:id>')
def download(id):
    file_data = FileContents.query.filter_by(id=id).first()
    print(file_data)

    enviar_arquivo = send_file(BytesIO(file_data.data), attachment_filename= f'arquivo.{file_data.formato}', as_attachment=True)
    return enviar_arquivo

@app.route('/delete/<int:id>')
def delete(id):
    file_data = FileContents.query.filter_by(id=id).first()
    db.session.delete(file_data)
    db.session.commit()
    return 'Arquivo: ' + file_data.name + ' removido com sucesso.' + '<br><a href="/">Voltar</a>'

