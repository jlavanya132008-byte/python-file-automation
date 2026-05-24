from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Python File Automation Project</h1>
    <p>Project Hosted Successfully on Render</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)