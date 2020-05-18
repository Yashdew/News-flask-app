from flask import *
import requests

app = Flask(__name__,template_folder='templates')

@app.route('/') 

def index():
    
    #url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=741da5d29d084a5b965e60c3648caaa3'
   
    #country = input("enter the Name of Country")
    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=741da5d29d084a5b965e60c3648caaa3')

    
    news = r.json()

    #print(news)

    """newsData ={
         'title' : news['articles']['title'],  
         'description' : news['articles']['description'],
         'url' : news['articles']['url'],
         'urlToImage' : news['articles']['urlToImage'],
         'publishedAt' : news['articles']['publishedAt']
            
        }"""
    title = news['articles'][0]['title'] 
    description = news['articles'][0]['description']
    url = news['articles'][0]['url']
    urlToImage = news['articles'][0]['urlToImage']
    publishedAt= news['articles'][0]['publishedAt']      
        
    print(title)        
        
    return render_template('index.html' , title = title , description = description , url = url , urlToImage = urlToImage , publishedAt= publishedAt )

def style():
    return render_template('style.css') 

if __name__ == '__main__':
    app.debug = True
    app.run()
