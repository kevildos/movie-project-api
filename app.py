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

# Class Model
class Movie(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    original_title = db.Column('original_title', db.String(80), unique=True, nullable=False)
    release_date = db.Column('release_date', db.String(80), nullable=False)
    overview = db.Column('overview', db.String(
        365), nullable=False)

    def __init__(self, original_title, release_date, overview):
        self.original_title = original_title
        self.release_date = release_date
        self.overview = overview

# Movie Schema
class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'original_title', 'release_date', 'overview')

# Init schema
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# Index
@app.route('/', methods=['GET'])
def index():
    return 'Flask!'

# Post Movie or Get All Movies
@app.route('/movie', methods=['GET','POST'])
def add_movie(): 
    if request.method == 'POST':
        original_title = request.json['original_title']
        release_date = request.json['release_date']
        overview = request.json['overview']

        new_movie = Movie(original_title, release_date, overview)

        db.session.add(new_movie)
        db.session.commit()

        return movie_schema.jsonify(new_movie)
    else:
        all_movies = Movie.query.all()
        result = movies_schema.dump(all_movies)
        return jsonify(result)

# Get Single Movie
@app.route('/movie/<id>', methods=['GET'])
def get_product(id):
    movie = Movie.query.get(id)
    return movie_schema.jsonify(movie)

#Update Movie
@app.route('/movie/<id>', methods=['PUT'])
def uprelease_date_movie(id): 
    movie = Movie.query.get(id)
    original_title = request.json['original_title']
    release_date = request.json['release_date']
    overview = request.json['overview']

    movie.original_title = original_title
    movie.release_date = release_date
    movie.overview = overview

    db.session.commit()

    return movie_schema.jsonify(movie)

# Delete Single Movie
@app.route('/movie/<name>', methods=['DELETE'])
def delete_product(name):
    movie = Movie.query.filter_by(original_title=name).first()
    
    db.session.delete(movie)
    db.session.commit()
    return movie_schema.jsonify(movie)

# Run Server
if __name__ == '__main__':

    app.run(debug=True)




