from flask.templating import render_template
from app import app

app.route('/')
def index():
  '''
  function that displays the landing page
  '''
  title = 'Welcome to Late News- Never miss a moment'
  return render_template('index.html', title = title)
