from config import *

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    formato = db.Column(db.String(80))
    data = db.Column(db.LargeBinary)

if os.path.exists(arquivobd):
    pass
else:
    db.create_all()
