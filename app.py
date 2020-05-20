from __future__ import unicode_literals
import subprocess
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
lnk = ''

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    print("The url address is '" + email + "'")
    global lnk
    lnk = email
    file1 = open("url.txt", "w")
    file1.write(email)
    file1.close()
    process = subprocess.Popen('py review_spi.py', shell=True)
    process.wait()
    return redirect('/')


# main driver
if __name__ == '__main__':
    # run app
    app.run(debug=True, threaded=True)