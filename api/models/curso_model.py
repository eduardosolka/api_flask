from api import db

class Curso(db.Model):
    __tablename__ = "tb_curso"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(length=50), nullable=False)
    descricao = db.Column(db.String(length=100), nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)