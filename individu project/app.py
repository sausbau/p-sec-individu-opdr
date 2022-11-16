from flask import *
from flask_recaptcha import *
import json
import os
from datetime import datetime

app = Flask(__name__)


app.config['RECAPTCHA_SITE_KEY'] = '6LcqNBoiAAAAAMfKgIhVmZugKL_XKR3eS9hm9H6e'
app.config['RECAPTCHA_SECRET_KEY'] = '6LcqNBoiAAAAAD7GEfeT4axoAq4HyiZq8OyTJswd'
recaptcha = ReCaptcha(app)


@app.route("/", methods=['GET', 'POST'])
def login():
    message = ''

    with open('database.json', 'r') as f:
        db = json.load(f)

    if request.method == 'POST':
        ip = request.environ['REMOTE_ADDR']
        with open ("ip.log", "a") as file:
            file.write(f"{datetime.now()} - {ip}\n") #write the ip and time to ip.log file to monitor the amount of post requests

        if recaptcha.verify():
                username = request.form["usname"]
                password = request.form["psw"]

                if username == db["username"]:
                    if password == db["password"] and db['F_attemps'] > 0:
                        db["F_attemps"] = 3
                        with open('database.json', 'w') as f:
                            json.dump(db, f)
                        return redirect(url_for('succes'))

                    elif  db['F_attemps'] <= 0:
                        Wmessage = 'Your account has been locked please contact us for more information'
                        return render_template('login.html', message=Wmessage)
                    else:
                        db["F_attemps"] -= 1
                        with open('database.json', 'w') as f:
                            json.dump(db, f)

                        Fmessage = f'You only have {db["F_attemps"]} attempt(s) left.'

                        return render_template('login.html', message=Fmessage)
                else:
                    message = "Your username or password is wrong"
                    return render_template('login.html', message=message)
        else:
            message = 'Please fill out the ReCaptcha!' 
    return render_template('login.html', message=message)

@app.route("/succes")
def succes():
    return render_template('succes.html')

@app.route("/token")
def token():
    return render_template('token.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


