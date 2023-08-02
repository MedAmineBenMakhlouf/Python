from flask import  render_template, redirect, request, flash,session
from flask_app import app
from flask_app.models.message import Message


@app.route('/messages/<int:msg_id>/destroy')
def delete_msg(msg_id):
    Message.delete({'id':msg_id})
    return redirect('/dashboard')

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'user_id' not in session:
        return redirect('/')
    Message.send(request.form)
    return redirect('/dashboard')