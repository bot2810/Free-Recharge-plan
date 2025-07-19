from flask import Flask, render_template
import os

# Static ও Template ফোল্ডার ঠিকভাবে নির্ধারণ
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/game')
def game():
    return render_template('index.html')

# Optional: Render/Debug Purpose
@app.route('/debug')
def debug():
    return {
        "cwd": os.getcwd(),
        "templates": os.listdir('templates'),
        "static": os.listdir('static')
    }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
