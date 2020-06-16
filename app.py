from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'


db = SQLAlchemy(app)


from routes import * 

if __name__=='__main__':
    app.run(debug=True)