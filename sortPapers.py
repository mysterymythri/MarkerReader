from ddlite import *
import article

def sortPapers(articles):
  for article in articles:
    article.score(biomarkerName, diseaseName)
  articles.sort(key=getScore)
  return articles
  
  
