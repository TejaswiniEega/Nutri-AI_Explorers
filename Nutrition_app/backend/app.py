import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

app = Flask(__name__)
CORS(app)

@app.route("/get-nutrition", methods=["POST"])
def get_nutrition():
    data = request.json
    food_item = data.get("food")

    if not food_item:
        return jsonify({"error": "Food item is required"}), 400

    try:
        response = genai.generate_text(f"Provide detailed nutritional information for {food_item}. Include macronutrients, micronutrients, and calories.")
        return jsonify({"nutrition": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
