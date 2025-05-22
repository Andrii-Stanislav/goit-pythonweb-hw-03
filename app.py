from flask import Flask, render_template, request, redirect, url_for, abort
from datetime import datetime
import json
import os

app = Flask(__name__)

# Ensure storage directory exists
if not os.path.exists('storage'):
    os.makedirs('storage')

# Initialize data.json if it doesn't exist
if not os.path.exists('storage/data.json'):
    with open('storage/data.json', 'w') as f:
        json.dump({}, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        message_text = request.form.get('message')
        
        if username and message_text:
            # Create timestamp
            timestamp = str(datetime.now())
            
            # Read existing data
            with open('storage/data.json', 'r') as f:
                data = json.load(f)
            
            # Add new message
            data[timestamp] = {
                "username": username,
                "message": message_text
            }
            
            # Write back to file
            with open('storage/data.json', 'w') as f:
                json.dump(data, f, indent=2)
            
            return redirect(url_for('index'))
    
    return render_template('message.html')

@app.route('/read')
def read():
    try:
        with open('storage/data.json', 'r') as f:
            messages = json.load(f)
        return render_template('read.html', messages=messages)
    except FileNotFoundError:
        return render_template('read.html', messages={})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) 