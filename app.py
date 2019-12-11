from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template("index.html")               

@app.route('/federations')
def federations():
    '''Return open feds. page'''
    return render_template("federations.html")

@app.route('/join')
def join():
    '''return join page'''
    return render_template("join.html")

@app.route('/topics')
def topics():
    '''return topics page'''
    return render_template('topics.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboards.html')


if __name__ == '__main__':
    app.run(debug=True)

