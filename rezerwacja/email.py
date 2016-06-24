from django.core.mail import send_mail

def send_email(dane):
    subject = dane['subject']
    message = dane['message']
    from_email = dane['from_email']

    send_mail(subject, message, from_email, ['admin@rezerwacja.com'])

