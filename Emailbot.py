import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('blablabla@gmail.com','xxxxx',)
    email = EmailMessage()
    email['From'] = 'blabla@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {

    'dad': 'hidad@gmail.com',
    'mom': 'himom@gmail.com',
    'sister': "hisis@gmail.com"

    }
def get_email_info():
    talk('To Whom you want to send the email?:')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of the email?')
    subject = get_info()
    talk("Tell me the text of the email: ")
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hi, you email is sent')
    talk('Do you want to send more emails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()


