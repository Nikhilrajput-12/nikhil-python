#Quickstart

# A Minimal Application
'''from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return "<p>Hello, World! welcome</p>"

def product():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True , port=5000)''' 

#external visible server
'''cmd=flask run --host=0.0.0.0'''

#1.running(GUNICORN)(server)

"SYNTAX"
'''{MODULE-IMPORT}:{APP_VARIABLE}'''
"ex =gunicorn app:app"  #cmd
#ex
'''from flask import Flask

def create_app():
    app =Flask(__name__)
    @app.route('/')
    def hello_world():
      return 'Hello, World!'
    
    return app
'''
"cmd = gunicorn -w 4 'app:app" # for no of processes to run

#BINDING externally

'''Running Gunicorn as the root user is risky because it means your application will also run with root privileges, which can be a security problem. To avoid this, you shouldn't use Gunicorn to directly handle traffic on standard web ports like 80 (HTTP) or 443 (HTTPS),
which normally require root access.
Instead, it's safer to use a reverse proxy like Nginx or Apache in front of Gunicorn. These tools can listen on ports 80 or 443 and then pass the requests to Gunicorn running on a different, non-privileged port (one that doesn't require root access).
If you need Gunicorn to listen on all network interfaces (all external IPs), you can use the -b 0.0.0.0 option, but only on a non-privileged port (like 8000). However, if you're using a reverse proxy setup, you should avoid binding Gunicorn to all external IPs like this, 
as it could allow someone to bypass the proxy and access your app directly, which can be a security risk.
'''
'''0.0.0.0 is not a valid address to navigate to, you’d use a specific IP address in your browser.'''
# Logs for each request aren’t shown by default, only worker info and errors are shown. 
# To show access logs on stdout, use the --access-logfile=- option.


#ASYNC WITH (GEVENT OR EVENTLET)

'''In simple terms, Gunicorn's default "sync" worker handles requests one at a time. This is fine for many web applications, especially when each request can be processed quickly.
However, if your app needs to handle many simultaneous connections or long-running tasks (like real-time chats or streaming data), the sync worker might not be the best choice.
 That's where asynchronous workers, like those using gevent or eventlet, come in.
These asynchronous workers allow your app to handle multiple tasks at the same time without waiting for one task to finish before starting another. But to take advantage of this,
 your code needs to be written in a way that supports these asynchronous operations (by using gevent or eventlet).
In summary, we use asynchronous workers when our app needs to manage many connections or long-running tasks at the same time, and our code is set up to handle it'''
#gevent

#cmd= gunicorn -k gevent 'app:create_app()'

#eventlet
#cmd = gunicorn -k evntlet 'app:create_app'

# 2.Waitress(server)

'''Waitress is a pure Python WSGI server.
It is easy to configure.
It supports Windows directly.
It is easy to install as it does not require additional dependencies or compilation.
It does not support streaming requests, full request data is always buffered.
It uses a single process with multiple thread workers.
This page outlines the basic'''
# $ pip install waitress
# cmd =$ waitress-serve --host 127.0.0.1 --call hello:create_app   call fun
#  cmd=waitress-serve --host 127.0.0.1 hello:app

'Serving on http://127.0.0.1:8080'
# Logs for each request aren’t shown, only errors are shown. 
# Logging can be configured through the Python interface instead of the command line.


#3.mod_wsgi(server)

''' mod_wsgi is a WSGI server integrated with the Apache httpd server.
The modern mod_wsgi-express command makes it easy to configure and start the server without needing to
 write Apache httpd configuration'''
'''from flask import Flask

hello = Flask(__name__)

@hello.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="__main__":
    hello.run(debug=True)'''


import random

def generate_number():
    return random.randint(1, 100)

def number_guessing_game():
    number_to_guess = generate_number()
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()