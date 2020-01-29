# MovieFinder API

A Flask(Python) RESTful API that stores movie information API to a miniature instance of a SQL database using SQLite.

The current operations include
* `/movie` to GET all movies in the database as a JSON
* `/movie/{id}` to GET a specific movie in the database by its id
* `/movie/{name}` to GET a specific movie in the database using it's name (includes whitespace characters)
* `/movie` to POST a new movie in the database following the JSON format
* `/movie/{id}` to PUT (update) a specific movie in the database by its id
* `/movie/{id}` to DELETE a specific movie in the database by its id
* `/movie/{name}` to DELETE a specific movie in the database using it's name (includes whitespace characters)


## Quick Start
The API can be accessed at http://movie-api-stage.herokuapp.com/

If you want to run the development build, clone the Github repository, start the virtual environment using `source env/bin/activate` and run `python3 app.py` in the root project directory.

## Status
The app can be accessed and used on the firebaseapp domain. I have plans to connect the API to a mySQL server to become more familiar with the technology, but since SQLite allows you to store 0.5MB, that is enough for my purposes.
