import os

from flask import Flask
from flask_mail import Mail, Message
from . import bp_home

MAIL = Mail()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Mail configuration
    app.config['MAIL_SERVER'] = "smtp.gmail.com"
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = "jesse.d.johnson.533@gmail.com"
    app.config['MAIL_PASSWORD'] = "qmey woxk ombp hndf"
    app.config['MAIL_DEFAULT_SENDER'] = "jesse.d.johnson.533@gmail.com"
    app.config['MAIL_DEBUG'] = False
    MAIL.init_app(app)

    app.register_blueprint(bp_home.bp)

    return app

def send_email(contact_form):
    try:
        message = Message(
            subject=f"PERSONAL WEBSITE MAIL - {contact_form['name']} - {contact_form['subject']}", 
            sender=contact_form["email"], 
            recipients=["jesse.d.johnson.533@gmail.com"]
        )
        message.body = f"""
            From: {contact_form["name"]}
            Email: {contact_form["email"]}

            Message: {contact_form["message"]}
            """
        
        MAIL.send(message)
    except Exception as e:
        print("ERROR - Failed to send email")