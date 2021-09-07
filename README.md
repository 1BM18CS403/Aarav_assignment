# Aarav_assignmentMails.py is the email file.
You can send the mails by using any domain within Google, Yahoo, Microsoft live

To run or send the mail, you need to import mails.py
1. Import package
	import mails
	
2. Load the function from mails
	m = mails.send_email
	
3. To send message please follow the below instructions
	There are 2 dictionaries you need to pass:
	1. auth
		username: for from mail id
		password: account password to login server
	2. data
		to: to account
		subject: subject of the mail
		text: Content or mime text you can send by mail
		
	Below is the sample code of standard code structure
  <code>
	mail = m(
        auth={"username":"YOUR_EMAIL","password":"YOUR_PASSWORD"},
         data={
             'to':'RECIPIENT_ID',
             'subject':'SUBJECT',
             'text':'CONTENT'
         })
	</code>
	mail will recieve TRUE if the message sent, FALSE if the credentials were wrond. 
	
The code iterates to correct server one by one to send the mail, if fails.
		
