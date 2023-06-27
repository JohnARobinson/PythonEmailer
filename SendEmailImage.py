import smtplib
import ssl
from email.message import EmailMessage
import imghdr
import keyboard

def emailUpdate():
    email_address = '*****************'
    email_password = '***************'
    email_receiver = '*****************'
    
    subject = 'Test Sending Image'
    body = """
    Image Comparison
    """
    
    em = EmailMessage()
    em['From'] = email_address
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    
    with open('sc1.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
        
    em.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, email_receiver, em.as_string())
        
emailUpdate()