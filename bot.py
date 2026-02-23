import requests
import os

# --- YOUR UPDATED CONFIGURATION ---
BOT_TOKEN = "8371746608:AAGXkauY6uJH7DwvhuvjkmSrjl4pJiux0Nc"
CHAT_ID = "8349642445"

def send_pdf_to_telegram(file_name):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    
    # Check if file exists before trying to send
    if not os.path.exists(file_name):
        print(f"❌ Error: I couldn't find a file named '{file_name}' in your folder.")
        print("Please make sure you have a PDF file in the same folder as this script.")
        return

    try:
        with open(file_name, 'rb') as doc:
            payload = {
                'chat_id': CHAT_ID, 
                'caption': f'📄 New Document: {file_name}\nProject: EthioTurkeyVisaCheck'
            }
            files = {'document': doc}
            
            print(f"🚀 Sending {file_name} to @EthioTurkeyVisaCheckBot...")
            response = requests.post(url, data=payload, files=files)
            
            if response.status_code == 200:
                result = response.json()
                file_id = result['result']['document']['file_id']
                print("-" * 30)
                print("✅ SUCCESS!")
                print(f"Check your Telegram. Your ID {CHAT_ID} should have a new message.")
                print(f"Telegram File ID: {file_id}")
                print("-" * 30)
            else:
                print(f"❌ Telegram API Error: {response.text}")
                
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# --- RUN THE UPLOAD ---
# Make sure you have a file named "passport.pdf" in your folder
# Or change "passport.pdf" below to match your file name!
send_pdf_to_telegram("passport.pdf")