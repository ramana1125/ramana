
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Store the user data in a database or file
        # Example: You might want to store this data in a database
        # db.store_user(name, email, password)
        return render_template('success.html')
    # If it's a GET request or if the form validation failed, render the registration form
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
