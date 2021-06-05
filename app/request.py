from _typeshed import IdentityFunction
from app.instance.config import API_KEY
from app import app
import urllib.request, json
from .models import ArticlesClass
from .models import SourcesClass

Articles = ArticlesClass.Articles
Sources = SourcesClass.Sources

#Getting Api key
api_key = API_KEY

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
    src_id = identification
  return source_results_list, src_id


def get_source_articles(source_id):
  '''
  function that gets articles from a given source
  '''
  
  get_articles = source_articles_url.format(source_id)
  with urllib.request.urlopen(get_articles) as url:
    articles_response = url.read()
    articles_response_readable = json.loads(articles_response)
    articles_results = None

    if articles_response_readable['articles']:
      get_articles_list = articles_response_readable['articles']
      articles_results = process_articles(get_articles_list)

  return articles_results

def process_articles(get_articles_list):
  '''
  function that gets data from api response
  '''
  articles_list = []
  for article in get_articles_list:
    author = article.get('author')
    title = article.get('title')
    description = article.get('description')
    url = article.get('url')
    image = article.get('urlToImage')
    date = article.get('publishedAt')
    content = article.get('content')

    new_article = Articles(author, title, description, url, image, date, content)
    articles_list.append(new_article)

  return articles_list