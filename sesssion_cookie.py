from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)
app.secret_key = "abhi"

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/submit', methods = ['POST'])
def submit():
    input = request.form
    res = make_response("Login Successfully!<br/><a href='/view'>View</a>")
    res.set_cookie('email', input['email'])
    session['email'] = input['email']
    return res
  
@app.route('/view')
def view():
    email = request.cookies.get('email')
    if 'email' in session:
        e = session['email']
    resp = make_response(render_template('view.html',email = email, e = e))
    return resp

if __name__  == "__main__":
    app.run(debug = True)