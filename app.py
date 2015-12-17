# -*- coding: utf-8 -*-

# Flask application to demo accepting payments via PayPal
# using the rest sdk for Python

import os
from flask import Flask, request, render_template
from flask_mail import Mail, Message
from datetime import datetime
import json

app = Flask(__name__)
app.config['MAIL_PASSWORD'] = os.getenv('SENDGRID_PASSWORD', 'r5mdhe6m7189')
app.config['MAIL_USERNAME'] = os.getenv('SENDGRID_USERNAME', 'app45165158@heroku.com')
app.config['MAIL_SERVER'] = "smtp.sendgrid.net"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = "hear-service@hear.herokuapp.com"
app.config['MAIL_DEBUG'] = 0
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPPRESS_SEND'] = None

mail = Mail(app)


@app.route('/', methods=['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT'])
def index():
    var_names = ('form', 'args', 'stream', 'headers', 'data', 'files', 'environ', 'method',
                 'path', 'script_root', 'url', 'base_url', 'url_root', 'is_xhr', 'blueprint', 'endpoint')
    vars = {var: getattr(request, var, '-') for var in var_names}
    vars['json'] = render_template('table.html', vars=request.get_json(silent=True))
    vars['cookies'] = render_template('table.html', vars=request.cookies)
    vars['headers'] = render_template('table.html', vars=request.headers)
    vars['environ'] =render_template('table.html', vars=request.environ)

    html = render_template('body.html', vars=vars, address=request.environ['REMOTE_ADDR'], referrer=request.referrer)

    msg = Message("Hear service report",
                  html=html,
                  recipients=["nosuchip@gmail.com"])
    mail.send(msg)

    return html

if __name__ == '__main__':
    app.run(debug=True)
