import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("*** Enviar email con GMail ***")

user = input("Cuenta de correo (gmail): ")
password = input("Contraseña: ")

# Para las cabeceras
remitente = input("From (ex: administrador <hola@gmail.com>: ")
destinatario = input("To, (ex: tecnico <mundo@gmail.com>: ")
asunto = input("Subject (ex: Asunto): ")
mensaje = input("Mensaje HTML: ")

# Host y puerto SMTP de Gmail
gmail = smtplib.SMTP('smtp.gmail.com', 587)

# Cifrado de datos requerido TLS
gmail.starttls()

# Credenciales del usuario
gmail.login(user, password)

# Despuración del envío 1 = true
gmail.set_debuglevel(1)

# Creamos cabeceras
header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

# Conversión a HTML del mensaje
mensaje = MIMEText(mensaje, 'html') #Content-type:text/html

# Añadimos mensaje a cabecera
header.attach(mensaje)

# Enviar
gmail.sendmail(remitente, destinatario, header.as_string())

# Cerramos la conexión SMTP
gmail.quit()