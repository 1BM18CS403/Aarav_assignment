# Libraries
import smtplib


def send_email(auth,data):
    # Trying to connect with theese servers, if the domain of of one server filed to connect
    # to the server
    smtp_dom = ['smtp.gmail.com','smtp.live.com','smtp.mail.yahoo.com']
    for i in smtp_dom:
        if (send(server=smtplib.SMTP(i,587),auth=auth, data=data))==False:
            return False
        else:
            return True
    
def send(server, auth, data):
    # Credentials to connect server
    username = auth.get('username')
    password = auth.get('password')
    # Starting server
    server.ehlo()
    server.starttls()
    # print("Server started")
    try:
        server.login(username, password)
        # print("Logged in")
    except Exception as e:
        print(e)
        pass

    # encoding data to message
    msg = 'Subject: {}\n\n{}'.format(data.get('subject'), data.get('text'))
    try:
        # Sending Mail
        server.sendmail(username, data.get('to'), msg)
        # print("sent mail")
        return True
    except:
        # Enters exception if server refuses tosend the mail
        # print("Retrying with another server")
        pass
    server.quit()
    # return json.dumps({'message':'success'})

