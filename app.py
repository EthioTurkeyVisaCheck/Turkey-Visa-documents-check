from flask import Flask, request, jsonify
from flask_cors import CORS # You need this to allow the browser to talk to Python
import requests

app = Flask(__name__)
CORS(app) # This prevents the "Blocked by CORS" error

BOT_TOKEN = "8371746608:AAGXkauY6uJH7DwvhuvjkmSrjl4pJiux0Nc"
CHAT_ID = "8349642445"

@app.route('/upload', methods=['POST'])
def upload():
    # Capture the data
    name = request.form.get("fullName")
    tg = request.form.get("telegram")
    ref = request.form.get("reference")
    age = request.form.get("age")
    bank = request.form.get("bankBalance")
    expiry = request.form.get("passportExpiry")
    
    # Send formatted text to Telegram
    msg = (f"🔔 **NEW VISA ASSESSMENT**\n"
           f"👤 Name: {name}\n"
           f"✈️ User: {tg}\n"
           f"🎂 Age: {age}\n"
           f"💰 Bank: {bank} ETB\n"
           f"📅 Expiry: {expiry}\n"
           f"🔢 Ref: `{ref}`")
    
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                  data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

    # Send PDFs
    files = request.files.getlist("files")
    for file in files:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument", 
                      data={"chat_id": CHAT_ID, "caption": f"📄 {file.filename}"}, 
                      files={"document": (file.filename, file.read())})

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)