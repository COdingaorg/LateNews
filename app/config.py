class Config:
  '''
  General configuraions
  '''
  SOURCE_NEWS_API = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  SOURCES_API = 'https://newsapi.org/v2/sources?apiKey={}'

class ProdConfig(Config):
  '''
  Configurations for production
  '''
  pass

class DevConfig(Config):
  '''
  Configurations for development
  '''
  
Debug = True