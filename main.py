import base64
import os
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    envelope = request.get_json()
    if not envelope:
        message = "no Pub/Sub message received."
        print(f"error: {message}")
        return (f"Bad Request: {message}", 400)
    if not isinstance(envelope, dict) or "message" not in envelope:
        message = "invalid Pub/Sub message format."
        print(f"error: {message}")
        return (f"Bad Request: {message}", 400)
    pubsub_message = envelope["message"]
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        decoded_message = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
    print(f"Received message: {decoded_message}")
    return ("", 200)

