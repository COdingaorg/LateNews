from flask.templating import render_template
from app import app
from .request import get_sources

sourcesSamples = get_sources()

@app.route('/')
def index():
  '''
  function that displays the landing page
  '''
  heading = 'Welcome to Late News-''Never miss a moment'

  return render_template('index.html', title = heading, sourceList = sourcesSamples)