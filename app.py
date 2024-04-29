from flask import Flask, request, jsonify, render_template

from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template('base.html')



@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    message = data['message']  # Extract message from request data
    response = get_response(message)  # Pass message string to get_response
    return jsonify({'answer': response})


if __name__ == "__main__":
    app.run(debug=True)