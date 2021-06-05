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

def process_results(sources_fetched_list):
  '''
  getting data from the json file and storing them in a variable
  '''
  source_results_list = []
  for source in sources_fetched_list:
    identification = source.get('id')
    name = source.get('name')
    description = source.get('description')
    url = source.get('url')
    category = source.get('category')
    language = source.get('language')
    country = source.get('country')
    
    new_source = Sources(identification, name, description, url, category, language, country)
    source_results_list.append(new_source)
  return source_results_list


