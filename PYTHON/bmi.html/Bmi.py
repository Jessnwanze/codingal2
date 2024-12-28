from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')

    if not weight or not height or weight <= 0 or height <= 0:
        return jsonify({'error': 'Invalid input'}), 400

    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        category = 'Normal weight'
    elif 25 <= bmi < 29.9:
        category = 'Overweight'
    else:
        category = 'Obese'
    
    return jsonify({'bmi': round(bmi, 2), 'category': category})

if __name__ == '__main__':
    app.run(debug=True)
