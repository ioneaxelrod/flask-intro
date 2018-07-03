"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
              <html>
                <p><a href="/hello">Compliments!
                </a></p>
                <p><a href="/diss">Surprises!
                </a></p>
              </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <p>What's your name? <input type="text" name="person"></p>
          <p>What's your compliment? 
          <select name="compliment">
            <option value="cute">Cute</option>
            <option value="smart">Smart</option>
            <option value="funny">Funny</option>
            <option value="frugal">Frugal</option>
          </p>
          <input type="submit" value="Submit">
        </form>

      </body>
    </html>
    """


@app.route('/diss')
def diss():
    """Say hello and prompt for user's name."""
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/dissed">
          <p>What's your name? <input type="text" name="person"></p>
          <input type="submit" value="Submit">
        </form>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player.title(), compliment.lower())


@app.route('/dissed')
def dissed():
    """Get user by name."""

    player = request.args.get("person")
    insults = ["ugly", "boring", "dumb", "Republican", "broke"]
    insult = choice(insults)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I heard you're {}!
      </body>
    </html>
    """.format(player.title(), insult.lower())


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
