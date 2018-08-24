from flask import Flask, render_template, request, redirect, url_for
from .database import content
from .models import custom, DBSession

app = Flask(__name__)

@app.route("/")
def welcome_listing():
    session = DBSession()
    content = session.query(custom).all()
    return render_template('index.html', content=content)

@app.route("/new")
def new_lister():
    return render_template('new_country.html')

@app.route("/create-nation", methods=["POST"])
def create_new_todo(*args, **kwargs):
    session = DBSession()
    td = TodoNote(title=request.form['title'], description=request.form['description'])
    session.add(td)
    session.commit()
    return redirect(url_for('list_of_todos'))

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'