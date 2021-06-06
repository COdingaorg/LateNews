from flask import Flask, render_template, request
from app import app
from .requests import get_sources, get_source_articles
from app import requests


@app.route('/')
def index():
  '''
  function that displays the landing page
  '''
  heading = 'Welcome to Late News'
  subheading = 'Never miss a moment'
  sourcesSamples = get_sources()
  return render_template('index.html', title = heading, sourceList = sourcesSamples, subhead = subheading)

@app.route('/source', methods = ['GET', 'POST'])
def source_articels():
  '''
  function that displays source articles
  '''
  if request.method == 'POST':
    src_id = request.form['id']

  articles = get_source_articles(src_id)

  return render_template('source.html', articleList = articles)