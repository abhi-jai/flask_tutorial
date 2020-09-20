from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# homepage
@app.route('/')
def home():
    return "Welcome to TechLifediary Home!"

# form
@app.route('/form')
def form():
    return render_template('form.html')

# submit form
@app.route('/submit', methods = ['POST'])
def submit():
    input = request.form
    return render_template('user.html',data = input)

# redirection
@app.route('/user/<type>')
def user(type):
    if type == 'form':
        return redirect(url_for('form'))
    if type == 'home':
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug = True)

