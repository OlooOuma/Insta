from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email():
    # Creating message subject and sender
    subject = 'Welcome to Instagram'
    sender = 'oloosolomon@gmail.com'
    print('Welcome to Instagram')
    #passing in the context vairables
    text_content = render_to_string('email/email.txt',)
    html_content = render_to_string('email/email.html',)

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()