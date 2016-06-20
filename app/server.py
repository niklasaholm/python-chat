from flask import render_template, session, url_for, redirect
from flask_socketio import emit, send
import uuid
from app import app, socketio




@app.route('/')
def index():
    return render_template('game.html')


@socketio.on('create user')
def create_user():
    session['username'] = str(uuid.uuid4())
    emit('new user', session['username'])

@socketio.on('message')
def message(message):
    emit('message', message, broadcast=True)

