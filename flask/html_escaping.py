
#HTML ESCAPING

'''When returning HTML (the default response type in Flask), 
any user-provided values rendered in the output must be escaped to protect from injection attacks. 
HTML templates rendered with Jinja, introduced later, will do this automatically.
'''
'''from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.debug = True  # Enable debug mode

@app.route("/<name>")
def hello(name):
    return f"hello, {escape(name)}"

if __name__ == "__main__":
    app.run()

'''
#ROUTING

'''from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    return 'index page'

@app.route('/hello')
def hello():
    return 'hello world'

if __name__ == "__main__":
    app.run()'''


#VARIABLE RULES

'''from markupsafe import escape
from flask import Flask

app=Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return f'User  {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'subpath {escape(subpath)}'

if __name__ == "__main__":
    app.run()
'''

'''Converter types:

string =(default) accepts any text without a slash

int =accepts positive integers

float =accepts positive floating point values

path =like string but also accepts slashes

uuid = accepts UUID strings


'''

#UNIQUE URLs/ REDIRECTION BEHAVIOUR
'''
from flask import Flask

app=Flask(__name__)
app.debug=True

@app.route('/projects/')
def projects():
    return 'the project page'

@app.route("/about")
def about():
    return "the about page"

@app.errorhandler(404)
def page_not_found(a):
    return "Sorry, this page does not exist", 404

if __name__ == '__main__':
    app.run()

    '''

#URL Building  (url_for func)

'''from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))'''

#HTTP METHODS

'''from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)'''

'''@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would normally validate the user credentials
        return do_the_login()
    else:
        return show_the_login_form()
'''
'''@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
def do_the_login():
    # Placeholder for actual login logic
    return redirect(url_for('index'))

def show_the_login_form():
    # This would typically render a login form template
    return '<form method="post">Login Form</form>'

if __name__ == '__main__':
    app.run(debug=True)'''

from flask import Flask, request, jsonify

app = Flask(__name__)

# Route with GET and POST methods
'''@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return jsonify({"message": "This is a GET request"})
    
    if request.method == 'POST':
        data = request.json
        return jsonify({"message": "This is a POST request", "data": data})'''

# Route with PUT and DELETE methods
'''@app.route('/example/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete(id):
    if request.method == 'PUT':
        data = request.json
        return jsonify({"message": f"Resource {id} updated", "data": data})
    
    if request.method == 'DELETE':
        return jsonify({"message": f"Resource {id} deleted"})

if __name__ == '__main__':
    app.run(debug=True)
'''