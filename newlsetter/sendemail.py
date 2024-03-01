import smtplib

# Connexion au serveur SMTP de Gmail
smtp_server_domain_name = 'smtp.gmail.com'
port = 465
server = smtplib.SMTP_SSL(smtp_server_domain_name, port)

# Connexion avec votre adresse e-mail et mot de passe
sender_email = 'sea.star.debut@gmail.com'
password = 'Acces_Bruno2024'
server.login(sender_email, password)

# Créez le message à envoyer
recipient_email = 'mak302@gmail.com'
subject = 'premier test'
body = 'ce mail a été envoyé automatiquement par un programme. cest le premier test'
message = f'Subject: {subject}\n\n{body}'

# Envoyez l'e-mail
server.sendmail(sender_email, recipient_email, message)

# Fermez la connexion
server.quit()
