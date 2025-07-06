import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

# Ensure project root is in the Python path so imports work when executed from the app folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.chatbot_model import ChatMedBot
from utils import download_file

# Download any example data if needed
csv_url = "https://raw.githubusercontent.com/bhanuprakash-vangala/public-datasets/main/symptoms_example.csv"
# Save data in the shared data directory one level above this file
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_path = os.path.join(base_dir, 'data', 'symptoms_example.csv')
download_file(csv_url, data_path)

app = Flask(__name__)
CORS(app)

bot = ChatMedBot()

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = bot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
