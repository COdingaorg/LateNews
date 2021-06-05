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
  


