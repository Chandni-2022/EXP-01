from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client['user_registration']
users_collection = db['users']

@app.route('/')
def index():
    return render_template('reg.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        print("Form Data:", request.form)

        # Get form data
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        gender = request.form.get('gender')

        # Validation
        if not name or not username or not email or not phone or not password or not gender:
            return jsonify({'error': 'All fields are required'}), 400

        # Check for existing email or phone number
        if users_collection.find_one({"email": email}) or users_collection.find_one({"phone": phone}):
            return jsonify({'error': 'Email or Phone number already registered'}), 400

        # Hash password before storing
        hashed_password = generate_password_hash(password)

        # Insert into MongoDB
        user = {
            'name': name,
            'username': username,
            'email': email,
            'phone': phone,
            'password': hashed_password,
            'gender': gender
        }
        users_collection.insert_one(user)
        return jsonify({'message': 'Registration Successful'}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
