from app import app
import urllib.request, json
from .models import ArticlesClass
from .models import SourcesClass

Articles = ArticlesClass.Articles
Sources = SourcesClass.Sources

#Getting Api key
api_key = app.config['API_KEY']

#Getting base url
source_url = app.config['SOURCES_API']
source_articles_url = app.config['SOURCE_NEWS_API']

#get sources from api
def get_sources():
  '''
  Function that gets news sources from the api
  '''
  get_sources_response = source_url.format(api_key)
  with urllib.request.urlopen(get_sources_response) as url:
    sources_response = url.read()
    sources_response_readable = json.loads(sources_response)
    sources_results = None 

    if sources_response_readable['sources']:
      sources_fetched_list = sources_response_readable['sources']
      sources_results = process_results(sources_fetched_list)

  return sources_results







