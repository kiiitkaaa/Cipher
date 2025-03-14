import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from email.mime.text import MIMEText

# Области доступа Gmail API для отправки почты
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    """Аутентифицирует пользователя и возвращает сервис Gmail API."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        # Возвращаем объект сервиса для использования API Gmail
        service = build("gmail", "v1", credentials=creds)
        return service
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def create_message(sender, to, subject, message_text):
    """Создает сообщение в формате MIME и кодирует его для Gmail API."""
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return {'raw': raw}

def send_email(service, sender_email, recipient_email, subject, message_text):
    """Отправляет письмо с помощью Gmail API."""
    try:
        message = create_message(sender_email, recipient_email, subject, message_text)
        sent_message = service.users().messages().send(userId="me", body=message).execute()
        print(f'Письмо отправлено! ID сообщения: {sent_message["id"]}')
        return sent_message
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def send_user_mail(recipient_email, message_text):
    # Аутентификация и создание сервиса Gmail API
    service = authenticate_gmail()
    if service:
        # Запрашиваем данные для письма у пользователя
        sender_email = "businesskiiitkaaa@gmail.com"
        subject = "Зашифрованный текст"

        # Отправляем письмо
        try:
          send_email(service, sender_email, recipient_email, subject, message_text)
          return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False