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
    with open('database.json', 'r') as f: #here it wil open the json file with the database entries
        db = json.load(f)

    if request.method == 'POST':
        ip = request.environ['REMOTE_ADDR']
        with open ("ip.log", "a") as file:
            file.write(f"{datetime.now()} - {ip}\n") #write the ip and time to ip.log file to monitor the amount of post requests (login attempts)

        if recaptcha.verify(): #here it wil check if the captcha is verified or not
                username = request.form["usname"]
                password = request.form["psw"]

                if username == db["username"]: #if the username input is in the json file it executes the code here underneath
                    if password == db["password"] and db['F_attemps'] > 0: #if the password is correct and the attempts is higher than 0 
                        db["F_attemps"] = 3 #here it resets the number back to 3 if the username and password are correct of the user
                        with open('database.json', 'w') as f: #here it writes the 3 to the json file
                            json.dump(db, f)
                        return redirect(url_for('succes'))

                    elif  db['F_attemps'] <= 0: #here it checks if the amount of attempts is lower than 0 or is 0 if thats the case it will print the message underneath
                        Wmessage = 'Your account has been locked please contact us for more information'
                        return render_template('login.html', message=Wmessage)
                    else:
                        db["F_attemps"] -= 1 #if the password is incorrect of the user it wil reduce the ammount of attempts by 1 
                        with open('database.json', 'w') as f:
                            json.dump(db, f)

                        Fmessage = f'You only have {db["F_attemps"]} attempt(s) left.' #here it wil print the amount of attempts you have left

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


