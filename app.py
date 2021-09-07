from os import stat
from flask import Flask, request, jsonify, make_response
from flask.helpers import flash
from flask.templating import render_template
from werkzeug.utils import redirect

import mails

m = mails.send_email
app = Flask(__name__)

app = Flask("Restful API")
app.secret_key = "mailapi"

@app.route('/')
def index():
    return render_template('index.html') 

# You can test rest api in POSTMAN Api

@app.route('/send', methods=["POST"])
def api_detect():
    email_from = request.form["from"]
    email_to = request.form["to"]
    subject = request.form["subject"]
    
    if (send_mail.send_mail(email_from, email_to, subject)):
        response = jsonify({'message':'success'})
    else:
        send_mail.send_mail(email_from, email_to, subject)
    return make_response(response, 200)

@app.route('/send_mail', methods=["POST"])
def send_mail():
    email_to = request.form["email"]
    subject = request.form["subject"]
    text = request.form["text"]
    
    status = m(auth={"username":"ashokashu300@gmail.com","password":"9916315365Aa"},
                data={
                    'to':email_to,
                    'subject':subject,
                    'text':text
                }
            )
    print(status)
    if (status==True):
        flash("Mail Sent")
        return redirect('/')
    else:
        flash("Unexpected Error")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)