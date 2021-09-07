import mails
m = mails.send_email

mail = m(
        auth={"username":"YOUR_EMAIL","password":"YOUR_PASSWORD"},
         data={
             'to':'ashok.cs18@bmsce.ac.in',
             'subject':'Greet',
             'text':'Do you know what is happening'
         })
print(mail)