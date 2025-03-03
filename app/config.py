import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    FLASK_RUN_PORT=5000
    FLASK_RUN_HOST= '127.0.0.1'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'b6b4babaf2107f2064c516c88184c1f5483f62879c3330c0')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'sandbox.smtp.mailtrap.io')
    MAIL_PORT = os.environ.get('MAIL_PORT', '2525')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '2f6ff6b71f60b9')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'b270327f7e6b5c')
    MAIL_USE_TLS = True 
    MAIL_USE_SSL = False 
