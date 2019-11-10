import os

from flask import Flask, session, flash, render_template, request
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# list of channels; initialize with one "main" channel
channels = []
channels.append("main")

@app.route("/")
def index():
    return render_template("flack.html", channels=channels)

@app.route("/createChannel", methods=["POST"])
def createChannel():
    """Create a new chat channel"""
    channel = request.form.get("newchannel")
    channels.append(channel)
    print(f"ADDED NEW CHANNEL: {channel}")
    
    return render_template("flack.html", channels=channels)