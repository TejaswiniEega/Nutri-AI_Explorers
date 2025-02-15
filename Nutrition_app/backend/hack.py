# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Generative AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def get_nutritional_info(food_item):
    prompt = f"""Provide detailed nutritional information for {food_item} in this exact JSON format:
    {{
        "food_item": "{food_item}",
        "calories": "(value with unit)",
        "macronutrients": {{
            "protein": "(value with unit)",
            "fat": "(value with unit)",
            "carbohydrates": "(value with unit)"
        }},
        "micronutrients": {{
            "vitamins": ["list", "of", "vitamins"],
            "minerals": ["list", "of", "minerals"]
        }},
        "health_benefits": "(brief description)",
        "serving_suggestion": "(typical serving size)"
    }}
    If information is unavailable, use 'Unknown' as the value."""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        food_item = request.form['food_item']
        nutritional_data = get_nutritional_info(food_item)
        return render_template('index.html', 
                             food_item=food_item,
                             data=nutritional_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)