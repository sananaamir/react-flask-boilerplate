from flask import (Flask, render_template)

app = Flask(__name__)

# Disable static file caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template("index.html")