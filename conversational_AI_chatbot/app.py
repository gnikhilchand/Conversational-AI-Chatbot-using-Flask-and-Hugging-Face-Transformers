from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load Hugging Face conversational model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Route for the main page
@app.route("/")
def home():
    return render_template("index.html")

# Route for generating responses
@app.route("/get_response", methods=["GET"])
def get_response():
    user_message = request.args.get("msg", "").strip()
    if not user_message:
        return jsonify({"error": "Message is empty"}), 400

    try:
        response = chatbot(user_message)
        bot_response = response[0]["generated_text"]
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)



# from openai import OpenAI

# client = OpenAI(
#   api_key="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"
# )

# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "user", "content": "write a haiku about ai"}
#   ]
# )

# print(completion.choices[0].message);
