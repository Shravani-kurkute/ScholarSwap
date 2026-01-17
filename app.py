from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'your-api-key'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Message content is required"}), 400
    
    try:
        # Generate AI response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User: {user_message}\nAI:",
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
