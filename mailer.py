import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time

# Credenciales de Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('nombre_del_archivo.json', scope)
client = gspread.authorize(creds)

# Acceder a la hoja de cálculo
sheet = client.open('nombre_de_la_hoja_de_calculo').sheet1

# Obtener la lista de direcciones de correo electrónico
email_list = sheet.col_values(1)

# Configuración de correo electrónico
email_address = 'tu_direccion_de_correo_electronico@gmail.com'
email_password = 'tu_contraseña_de_gmail'

msg = MIMEMultipart()
msg['From'] = email_address
msg['Subject'] = 'Asunto del correo electrónico'

# Agregar imagen al correo electrónico (opcional)
#with open('ruta_de_la_imagen.jpg', 'rb') as f:
#    img_data = f.read()
#    image = MIMEImage(img_data)
#    msg.attach(image)

# Cuerpo del correo electrónico
body = 'Cuerpo del correo electrónico'

# Agregar el cuerpo del correo electrónico
msg.attach(MIMEText(body, 'plain'))

# Enviar correos electrónicos a la lista de direcciones
for email in email_list:
    # Configuración del servidor SMTP de Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)

    # Crear el mensaje y enviarlo
    msg['To'] = email
    server.sendmail(email_address, email, msg.as_string())
    print('Correo electrónico enviado a', email)

    # Esperar 1 minuto antes de enviar el siguiente correo electrónico
    time.sleep(60)

    # Cerrar la conexión con el servidor SMTP
    server.quit()

print('Todos los correos electrónicos han sido enviados')
