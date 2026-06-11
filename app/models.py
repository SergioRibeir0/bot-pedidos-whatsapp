from datetime import datetime
from app.database import db


class Pedido(db.Model):
    __tablename__ = "pedidos"

    id              = db.Column(db.Integer, primary_key=True)
    cliente_contato = db.Column(db.String(50), nullable=False)
    descricao       = db.Column(db.Text, nullable=False)
    status          = db.Column(db.String(30), nullable=False, default="Pendente")
    data_criacao    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Pedido id={self.id} cliente={self.cliente_contato} status={self.status}>"