from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace this with your actual AI model or API
def generate_response(prompt):
    # Simulate an AI response for now
    return f"You said: '{prompt}'. Here's a response: ..."

@app.route('/')
def index():
    return render_template('../templates/index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    ai_response = generate_response(user_message)
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)