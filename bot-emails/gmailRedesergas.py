import smtplib
import email.message

#crição do email 

def SendEmail():
    body_email = ''''
    <p>Olá Cauã,</p>
    <p>Email automatico, tenha um bom dia!</p>
    '''
    green_highlighter = '\033[1;36;42m'
    
    #Abrir email e enviar    
    msg = email.message.Message()
    msg['Subject'] = 'Teste envio de email com python'
    msg['From'] = '##############@gmail.com'
    msg['To'] = 'sendmail@sergipegas.com.br'
    senha = 'akvcqskunyxhkpuz'
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email)
    
    s = smtplib.SMTP('##########.com.br:25')
    s.connect('malibu', 25)
    s.ehlo()
    s.sendmail (msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print (f'{green_highlighter}Sent email!')
    
SendEmail()
