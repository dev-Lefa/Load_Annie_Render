from open_webui import OpenWebUI

app = OpenWebUI()

@app.route("/")
def home():
    return "Hello, OpenWebUI on Vercel!"
