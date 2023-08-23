import base64
import hashlib
import calendar
import datetime
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/secure/<filename>")
def secure(filename):
    secret = "secret"

    future = datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
    expiry = calendar.timegm(future.timetuple())

    secure_link = f"{expiry} /download/{filename} {secret}".encode('utf-8')
    print(secure_link)

    hash = hashlib.md5(secure_link).digest()
    base64_hash = base64.urlsafe_b64encode(hash)
    str_hash = base64_hash.decode('utf-8').rstrip('=')
    return redirect(f"/download/{filename}?md5={str_hash}&expires={expiry}")
