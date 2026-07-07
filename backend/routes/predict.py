from flask import Blueprint, request, jsonify
from services.model_service import predict_career
from database import save_prediction, get_all_predictions, get_prediction_count
from services.model_service import CAREER_DATA

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    try:
        data = request.get_json()
        name = data.get('name', 'User')
        skills = data.get('skills', '')
        if not skills:
            return jsonify({"error": "Skills required"}), 400

        result = predict_career(name, skills)

        # Save to SQLite database
        save_prediction(
            user_name=name,
            skills=skills,
            recommended_career=result["recommended_career"],
            confidence=result["confidence"]
        )

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@predict_bp.route('/history', methods=['GET'])
def get_history():
    try:
        predictions = get_all_predictions()
        # Format for frontend compatibility
        history = []
        for p in predictions:
            history.append({
                "id": p["id"],
                "date": p["date"],
                "name": p["user_name"],
                "skills": p["skills"],
                "recommended_career": p["recommended_career"],
                "confidence": p["confidence"]
            })
        return jsonify(history)
    except Exception as e:
        return jsonify([])

@predict_bp.route('/careers', methods=['GET'])
def get_careers():
    try:
        careers = []
        for career, data in CAREER_DATA.items():
            careers.append({
                "name": career,
                "salary": data["salary"],
                "required_skills": data["required_skills"][:5]
            })
        return jsonify(careers)
    except Exception as e:
        return jsonify([])

@predict_bp.route('/stats', methods=['GET'])
def get_stats():
    try:
        count = get_prediction_count()
        return jsonify({"total_predictions": count})
    except:
        return jsonify({"total_predictions": 0})
