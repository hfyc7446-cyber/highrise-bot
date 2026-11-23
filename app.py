import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

subprocess.Popen(["highrise", "bot:MyBot", "6b047f0685fb1bce83565220", "ac18f1ab60444932aad73394834e7f735be313e1cf36aaa5f90f2070c18a9dd4"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
