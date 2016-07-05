from ddlite import *
import article

def sortPapers(articles):
  for article in articles:
    article.score()
  articles.sort(key=getScore)
  return articles
  
  
