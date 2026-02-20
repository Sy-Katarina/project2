from flask import Flask, request
from google import genai

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

@app.route("/")
def home():
    return """
    <h2>Simple AI Assistant</h2>
    <form method="post" action="/chat">
        <input name="message" placeholder="Ask something..." style="width:70%;" />
        <button type="submit">Send</button>
    </form>
    """

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form.get("message", "")
    if not message.strip():
        return "No message provided", 400

    resp = client.models.generate_content(
        model="gemini-flash-latest",
        contents=message
    )

    return f"<h3>Response:</h3><p>{resp.text}</p><br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)