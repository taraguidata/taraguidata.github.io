from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    if not name or not email or not subject or not message:
        return "Faltan campos requeridos", 400

    # Cuerpo del mensaje
    full_message = f"""
    Has recibido un nuevo mensaje desde el formulario de contacto.

    Nombre/Empresa: {name}
    Email: {email}
    Asunto: {subject}

    Mensaje:
    {message}
    """

    # Crear el email
    msg = MIMEText(full_message)
    msg['Subject'] = subject
    msg['From'] = os.environ.get("taraguidata@gmail.com")         # Tu correo (seguro)
    msg['To'] = os.environ.get("taraguidata@gmail.com")             # Destinatario final
    msg['Reply-To'] = email                           # Quien completó el formulario

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(os.environ.get("MAIL_FROM"), os.environ.get("MAIL_PASSWORD"))
            server.send_message(msg)
        return "OK"
    except Exception as e:
        return str(e), 500

