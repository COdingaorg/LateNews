from flask import Flask, render_template, request, url_for
from . import main
from ..requests import get_sources, get_source_articles


@main.route('/')
def index():
  '''
  function that displays the landing page
  '''
  heading = 'Welcome to Late News'
  subheading = 'Never miss a moment'
  sourcesSamples = get_sources()
  return render_template('index.html', title = heading, sourceList = sourcesSamples, subhead = subheading)

@main.route('/source/<str:sid>')
def source_articels():
  '''
  function that displays source articles
  '''

  articles = get_source_articles({}).format(sid)

  return render_template('source.html', articleList = articles)

