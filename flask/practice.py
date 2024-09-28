'''from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    secret ="nikhil@123"
    get_secret=request.args.get('secret')
   
    dic ={"punjab":"chandigarh",
          "himachal" :"shimla",
          "jammu" :"srinagar"
          }
    

    if secret == get_secret:
        return jsonify(dic)
    
    else:
        return jsonify('not found')
    
   

if __name__ == '__main__':
    app.run(debug=True)
'''
'''from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)

# Secret key for encoding the JWT
app.config['SECRET_KEY'] = 'your_secret_key'

# Route to generate the token using GET method
@app.route('/generate-token', methods=['GET'])
def generate_token():
    # Get username from query parameters, default to 'default_user' if not provided
    username = request.args.get('username', 'default_user')
    
    # Set expiration time to 1 hour from now
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    
    # Create the payload with an expiration time
    payload = {
        'username': username,
        'exp': expiration
    }
    
    # Encode the token using the secret key
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    
    return jsonify({'token': token})

# Route to verify the token (still using POST method)
@app.route('/verify-token', methods=['POST'])
def verify_token():
    token = request.get_json().get('token')
    try:
        # Decode the token using the secret key
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'mespassword': 'Token is valid for that time', 'data': payload})
    except jwt.ExpiredSignatureError:
        return jsonify({'mespassword': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'mespassword': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True)'''



#dataabse

import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

def create_connection():
    """Create and return a database connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydatabase"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/create_user', methods=['POST'])
def create_user_info():
    # Get query parameters
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    # Check if both parameters are provided
    if not name or not password:
        return jsonify({'error': 'Both name and password parameters are required'}), 400

    # Check if the username already exists in the database
    connection = create_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    cursor = None
    try:
        cursor = connection.cursor(buffered=True)  # Use a buffered cursor
        check_query = "SELECT * FROM users WHERE name = %s"
        cursor.execute(check_query, (name,))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({'error': 'Username already exists. Please choose a different name.'}), 400

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Insert new user data into MySQL table
        insert_query = "INSERT INTO users (name, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, hashed_password))
        connection.commit()
        response = "Inserted successfully"
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to insert data into the database'}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return jsonify({'message': response})


@app.route('/verify_user', methods=['POST'])
def verify_user():
    # Get query parameters
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    # Check if both parameters are provided
    if not name or not password:
        return jsonify({'error': 'Both name and password parameters are required'}), 400

    # Retrieve stored hashed password from the database
    connection = create_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    cursor = None
    try:
        cursor = connection.cursor()
        select_query = "SELECT password FROM users WHERE name = %s"
        cursor.execute(select_query, (name,))
        result = cursor.fetchone()

        if result is None:
            return jsonify({'error': 'User not found'}), 404

        stored_hashed_password = result[0]

        # Verify the password
        if check_password_hash(stored_hashed_password, password):
            return jsonify({'message': 'User verified successfully'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401

    except Error as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to verify user credentials'}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    
def create_table():
    """Create the users table if it does not already exist."""
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print("Table created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()



if __name__ == '__main__':
    create_table()
    print(create_connection())
    app.run(debug=True)
