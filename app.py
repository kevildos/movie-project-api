from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Init db
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite://///' + os.path.join(basedir, 'db.sqlite'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Index
@app.route('/', methods=['GET'])
def index():
    return 'Flask!'

# Post Movie
@app.route('/movie', methods=['GET','POST'])
def add_movie(): 
    if request.method == 'POST':
        name = request.json['name']
        date = request.json['date']
        description = request.json['description']

        new_movie = Movie(name, date, description)

        db.session.add(new_movie)
        db.session.commit()

        return movie_schema.jsonify(new_movie)
    else:
        return 'You did it!'

# Run Server
if __name__ == '__main__':

    app.run(debug=True)


# Class Model
class Movie(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(80), unique=True, nullable=False)
    date = db.Column('date', db.String(80), unique=True, nullable=False)
    description = db.Column('description', db.String(
        365), unique=True, nullable=False)

    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description

# Movie Schema


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'date', 'description')


# Init schema
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
