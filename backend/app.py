from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os, sys

sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__,
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'),
    static_url_path='')
CORS(app, origins="*")

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'login.html')

# Register blueprints
from routes.predict import predict_bp
app.register_blueprint(predict_bp, url_prefix='/api')

# Import database functions
from database import create_user, get_user_by_email, init_db

# Initialize database
init_db()

# ===== AUTH ROUTES =====
@app.route('/api/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    data = request.get_json()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    skills = data.get('skills', '')

    if not name or not email or not password:
        return jsonify({"error": "Name, email and password required"}), 400

    # Check if email exists
    existing = get_user_by_email(email)
    if existing:
        return jsonify({"error": "Email already exists"}), 400

    user = create_user(name, email, password, skills)
    if user:
        return jsonify({
            "message": "Registered successfully",
            "user": {"name": user["name"], "email": email, "id": user["id"]}
        })
    return jsonify({"error": "Registration failed"}), 500

@app.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    data = request.get_json()
    email = data.get('email', '')
    password = data.get('password', '')

    user = get_user_by_email(email)
    if not user or user['password'] != password:
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "skills": user.get("skills", "")
        }
    })

@app.route('/api/profile', methods=['GET'])
def profile():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email required"}), 400
    user = get_user_by_email(email)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "name": user["name"],
        "email": user["email"],
        "skills": user.get("skills", ""),
        "joined": user.get("joined", "")
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "FutureMap AI is running!",
        "version": "2.0.0",
        "database": "SQLite"
    })

if __name__ == '__main__':
    print("Starting FutureMap AI with SQLite Database...")
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
