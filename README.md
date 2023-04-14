# mailer
Cómo enviar email de newsletter a clientes

El envío masivo de correos electrónicos promocionales puede ser considerado como spam si los destinatarios no han dado su consentimiento expreso y voluntario para recibir estos correos electrónicos. Por lo tanto, antes de enviar cualquier correo electrónico promocional, es importante obtener el consentimiento previo y explícito de los destinatarios para evitar problemas legales y de reputación.

Dicho esto, si cuentas con el consentimiento previo y voluntario de los destinatarios, puedes usar la biblioteca de Python gspread para acceder a los datos de un archivo de hoja de cálculo de Google y la biblioteca smtplib para enviar correos electrónicos a través de Gmail.

En este ejemplo, primero se accede a la hoja de cálculo de Google que contiene las direcciones de correo electrónico, luego se configura el correo electrónico utilizando la biblioteca smtplib y se envía a cada dirección de correo electrónico en la lista utilizando un ciclo for. También se agrega una pausa de 1 minuto entre cada envío para evitar el envío masivo y asegurarse de que los correos electrónicos sean entregados correctamente.

Recuerda que es importante cumplir con las regulaciones de protección de datos
