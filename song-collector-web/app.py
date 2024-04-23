from flask import Flask, render_template, request
from sqs import send_queue_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.get_json().get("message")
        if "http" in message:
            send_queue_message(message)
            return "Message sent successfully", 200
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
