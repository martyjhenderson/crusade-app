# Crusade Manager App

## What is it

A lazy logging tool so that we can keep track of our Warhammer 40k Crusade Games.

## Is it ready?

That's a big ole nope.

## How to use it

  * Copy it down
  * Create a venv
  * Install the requirements.txt
  * Setup the sqllitedb with `FLASK_APP=manager flask db init`
    * It may error, and I am working on that
  * Run the database migrations with `FLASK_APP=manager flask db upgrade`
  * Start it up with `FLASK_APP=manager flask run`
  * When you go to http://localhost:5000 it will redirect you. Be sure to register yourself.

## Bugs and Contributions

I am still getting the first round of this done - hold off on the floodgates.

## Thanks

* Thanks to [Koji Mochizuki](https://github.com/kjmczk) for their [tutorial](https://medium.com/technest/build-a-crud-app-with-flask-bootstrap-heroku-60dfa3a788e8)
* Thanks to [Miguel Grinberg](https://github.com/miguelgrinberg) for his [Mega-Tutorial on Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)