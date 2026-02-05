from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    password = request.form.get('password')
    score = 0
    feedback = []

    # 1. Check Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Needs 8+ characters")

    # 2. Check for Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number")

    # 3. Check for Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # 4. Check for Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a symbol (!@#$)")

    # Determine Result based on score
    if score == 4:
        result = "✅ STRONG: You have a bulletproof shield!"
        color = "#00ff00" # Green
    elif score >= 2:
        result = "⚠️ MEDIUM: Almost there! " + " | ".join(feedback)
        color = "#ffcc00" # Yellow
    else:
        result = "❌ WEAK: " + " | ".join(feedback)
        color = "#ff4444" # Red
        
    return render_template('index.html', result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)