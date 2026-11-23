import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

ROOM_ID = "6ae9987b659711f902db7e20"
BOT_TOKEN = "ac18f1ab60444932aad73394834e7f735be313e1cf36aaa5f90f2070c18a9dd4"

subprocess.Popen(["highrise", "bot:MyBot", ROOM_ID, BOT_TOKEN])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
