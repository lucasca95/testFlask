from flask import Flask, url_for, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            instance_relative_config=False,
            template_folder="templates",
            static_folder="static"
            )
app.config.from_object('config.Config')      # Config from object

db = SQLAlchemy()

@app.route('/', methods=['GET'])
def home():
    return "Home"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5555)