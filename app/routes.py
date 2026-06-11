import logging
from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from app.database import db
from app.models import Pedido

logger = logging.getLogger(__name__)
bp = Blueprint("whatsapp", __name__)


def _build_twiml(mensagem: str) -> str:
    resp = MessagingResponse()
    resp.message(mensagem)
    return str(resp)


@bp.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get("Body", "").strip()
    from_number  = request.form.get("From", "").strip()

    logger.info("Mensagem recebida de %s: %s", from_number, incoming_msg)

    msg_lower = incoming_msg.lower()

    # Registrar novo pedido
    if "pedido" in msg_lower:
        try:
            novo_pedido = Pedido(
                cliente_contato=from_number,
                descricao=incoming_msg,
            )
            db.session.add(novo_pedido)
            db.session.commit()

            resposta = (
                f"✅ *Pedido #{novo_pedido.id} recebido com sucesso!*\n\n"
                f"📋 Descrição: {novo_pedido.descricao}\n"
                f"📌 Status: {novo_pedido.status}\n\n"
                "Envie *Status* a qualquer momento para acompanhar seu pedido."
            )
        except Exception as exc:
            db.session.rollback()
            logger.error("Erro ao salvar pedido: %s", exc)
            resposta = "⚠️ Erro ao registrar seu pedido. Tente novamente em instantes."

    # Consultar status do último pedido
    elif msg_lower == "status":
        ultimo = (
            Pedido.query
            .filter_by(cliente_contato=from_number)
            .order_by(Pedido.data_criacao.desc())
            .first()
        )
        if ultimo:
            resposta = (
                f"🔍 *Seu último pedido:*\n\n"
                f"🆔 #{ultimo.id}\n"
                f"📋 {ultimo.descricao}\n"
                f"📌 Status: *{ultimo.status}*\n"
                f"🕐 {ultimo.data_criacao.strftime('%d/%m/%Y %H:%M')}"
            )
        else:
            resposta = (
                "ℹ️ Nenhum pedido encontrado para seu número.\n"
                "Envie *Pedido* seguido da descrição para criar um."
            )

    # Fallback
    else:
        resposta = (
            "👋 Bem-vindo! Como posso ajudar?\n\n"
            "• *Pedido* + descrição → registrar novo pedido\n"
            "• *Status* → consultar seu último pedido"
        )

    return _build_twiml(resposta), 200, {"Content-Type": "application/xml"}