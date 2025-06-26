from flask import Flask, request, jsonify
import pandas as pd

# Load the CSV file (update the filename if different)
df = pd.read_csv("symptom_department_specialist.csv")

app = Flask(__name__)

@app.route('/get_department', methods=['POST'])
def get_department():
    data = request.get_json()
    symptom = data.get("symptom", "").strip().lower()

    match = df[df['Symptom'].str.lower() == symptom]

    if not match.empty:
        response = {
            "department": match.iloc[0]['Department'],
            "specialist": match.iloc[0]['Specialist']
        }
    else:
        response = {
            "department": "General Medicine",
            "specialist": "General Physician"
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
