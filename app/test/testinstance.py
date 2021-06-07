import unittest
from unittest.case import TestCase
from app.models import Sources
from app.models import Articles

Sources = Sources
Articles = Articles

class TestSources(unittest, TestCase):
  '''
  class test to check behaviour of source class
  '''
  def setUp(self):
    '''
    creating a source class instance every time a test is to run
    '''
    self.new_source = Sources('aljaseera','Al-Jazeera', 'description', 'url link', 'news category', 'language', 'country of origin')
    self.new_article = Articles('author', 'title', 'description', 'url', 'image_url', 'publishedAt', 'content')

  def test_sourcesinstance(self):
    '''
    test is a source instance is created
    '''
    self.assertTrue(isinstance(self.new_source,Sources))

  def test_articlesInstance(self):
    '''
    tests if an articles instance is created
    '''
    self.assertTrue(isinstance(self.new_article, Articles)) 

