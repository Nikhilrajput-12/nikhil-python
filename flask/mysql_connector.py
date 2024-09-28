import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify

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

@app.route('/na', methods=['GET'])
def insert_user_info():
    # Get query parameters
    name ,age = request.args.get('name') , request.args.get('age')
    # print(request.args)
    # age = request.args.get('age')
    
    # Check if both parameters are provided
    if not name or not age:
        return jsonify({'error': 'Both name and age parameters are required'}), 400

    # Validate age parameter
    try:
        age = int(age)
    except ValueError:
        return jsonify({'error': 'Age must be an integer'}), 400

    # Insert data into MySQL table
    connection = create_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, age))
        connection.commit()
        response = "Inserted"
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to insert data into the database'}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify({'message': response})


@app.route('/ga', methods=['GET'])
def get_user_info():
    # Get query parameters
    name = request.args.get('name')
    
    # Check if both parameters are provided
    if not name:
        return jsonify({'error': 'name parameter is required'}), 400

    # Validate age parameter
    try:
        name = str(name)
    except ValueError:
        return jsonify({'error': 'Name must be an string'}), 400

    # Insert data into MySQL table
    connection = create_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        select_query = "SELECT age FROM users WHERE name = %s"
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to get data from the database'}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify({'age': result})


@app.route('/uu', methods=['GET'])
def update_user_info():
    # Get query parameters
    name = request.args.get('name')
    new_age = request.args.get('new_age')

    # Check if both parameters are provided
    if not name or not new_age:
        return jsonify({'error': 'Both name and age parameters are required'}), 400

    # Validate age parameter
    try:
        new_age = int(new_age)
    except ValueError:
        return jsonify({'error': 'Age must be an integer'}), 400

    # Update data in MySQL table
    connection = create_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    try:
        cursor = connection.cursor()
        update_query = "UPDATE users SET age = %s WHERE name = %s"
        cursor.execute(update_query, (new_age, name))
        connection.commit()
        response = "Updated"
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to update data in the database'}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify({'message': response})


@app.route('/du' , methods=['GET'])
def delete_user():
    
    name = request.args.get('name')

    # Check 
    if not name :
        return jsonify({'error': 'name is required'}), 400
   
    
    try:
        name = str(name)
    except ValueError:
        return jsonify({'error': 'Name must be a string'}), 400

    # Delete data from MySQL table
    connection = create_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM users WHERE name = %s"
        cursor.execute(delete_query, (name,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'No user found with the given name'}), 404
        response = "Deleted"
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to delete data from the database'}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify({'message': response})
    
    
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
            age INT NOT NULL
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
    create_table()  # Create table before starting the Flask app
    app.run(debug=True)
