class Articles:
  '''
  class defining arguments for articles instances
  '''
  def __init__(self, author, title, description, url, image_url, publishedAt, content ):
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.image = image_url
    self.date = publishedAt
    self.content = content