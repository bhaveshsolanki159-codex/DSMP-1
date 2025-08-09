from flask import Flask, render_template, request, redirect
from data import Database
# render_template -> load html file
# request -> receive a data

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    # return "<h1 style='color:green'> Hello World </h1>"
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name =request.form.get('user_ka_naam')
    email =request.form.get('user_ka_email')
    password =request.form.get('user_ka_password')

    respones = db.insert(name,email,password)

    if respones: #1
        return render_template('login.html',message='Registration Successful, Kindly login to proceed')
    else:
        return render_template('register.html',message='Email Already Exists')
    
    return name + " " + email + " " + password

@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password') 

    response = db.search(email,password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message ='Incorrect Email Password')
    
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=["post"])
def perform_ner():
    text = request.form.get("user_text")
    
app.run(debug=True) #no need to run again and again due to debug
