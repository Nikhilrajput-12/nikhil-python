
'''from flask import Flask, render_template

app=Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="nikhil"):
    print("sucess")
    return render_template('child.html',person=name)

if __name__=="__main__":
    app.run(debug=True)'''

# ACCESING REQUEST DATA
'''from flask import Flask, request

app = Flask(__name__)

# Define a simple rou  te for demonstration purposes
@app.route('/hello', methods=['POST'])
def hello():
    return 'Hello, World!'

# Test the request context
with app.test_request_context('/hello', method='POST'):
    # Assertions to check the path and method
    assert request.path == '/hello'
    assert request.method == 'POST'
    # Additional assertions can be made based on the simulated request

if __name__ == '__main__':
    app.run(debug=True)'''

#THE REQUEST OBJECT
'''from flask import Flask,request,render_template

app=Flask(__name__)

def valid_login(username, password):
    # Dummy validation function
    return username == "nikhil" and password == "12345"

def log_the_user_in(username):
    return f"Welcome, {username}!"
@app.route('/login',methods=['POST','GET'])
def login():
    error=None
    if request.method=='POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'invalid username /password'

    return render_template('child.html',error = error)
                       
if __name__ == '__main__':
    app.run(debug=True)'''


#FILE UPLOAD
'''from flask import Flask,request,render_template,jsonify,redirect,url_for,abort
app=Flask(__name__)
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400

    # Save the file or do something with it
    file.save('/Users/nikhilsingh/Downloads/{file.filename}')

    return jsonify({"message": "File uploaded successfully", "filename": file.filename})

if __name__==('__main__'):
    app.run(debug=True)'''
#RIDIRECT AND ERRORS

'''from flask import Flask, abort, redirect, url_for, render_template

app = Flask(__name__)  # Initialize the Flask app

@app.route('/')
def index():
    # Redirect to the login route
    return redirect(url_for('login'))

@app.route('/login')
def login():
    # Abort with a 401 Unauthorized error
    abort(401)
    abort(404)
    # This line will never be executed due to abort above
    this_is_never_executed()

# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(error):
    # Render a custom 404 page template
    return render_template('page_not_found.html'), 404

# Error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized(error):
    # Render a custom 401 page template
    return render_template('unauthorized.html'), 401

if __name__ == '__main__':
    app.run(debug=True)
'''
'''from flask import Flask, render_template, make_response,url_for,abort
app = Flask(__name__)

@app.route('/')
def index():
    return "Home Page"

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(404)
def not_found(error):
    # Create a response object with a rendered template and a 404 status code
    resp = make_response(render_template('error.html'), 404)
    # Add a custom header to the response
    resp.headers['X-Some-Custom-Header'] = 'CustomValue'
    # Return the modified response object
    return resp

if __name__ == '__main__':
    app.run(debug=True)
'''

#API with JSON
'''from flask import Flask, url_for, jsonify

app = Flask(__name__)

# Define a simple User class
class User:
    def __init__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image = image

    def to_json(self):
        return {
            "username": self.username,
            "theme": self.theme,
            "image": url_for("user_image", filename=self.image)
        }

# Mock database of users (in-memory list of User objects)
users_db = [
    User("alice", "dark", "alice.png"),
    User("bob", "light", "bob.png"),
]

def get_current_user():
    """
    Simulate fetching the current user.
    In a real application, you would get the user from the session or request context.
    """
    return users_db[1]  # Here we are simply returning the first user for demonstration purposes.

def get_all_users():
    """
    Return all users in the mock database.
    """
    return users_db

# Route to get the current user's details
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

# Route to get all users
@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])

# Mock route to serve user images
@app.route("/user_image/<filename>")
def user_image(filename):
    """
    Mock endpoint to serve user images.
    In a real application, this would serve a file from the filesystem or cloud storage.
    """
    return f"Image file: {filename}"

if __name__ == "__main__":
    app.run(debug=True)
'''

#sessions
'''from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Store the username in the session
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return ''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    ''

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)'''


#MESSAGE FLASHING
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index_flashing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    
    # Return the login template with error (if any)
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
