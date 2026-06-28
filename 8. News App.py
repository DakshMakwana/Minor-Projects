"""use the NewsAPI and the requests module to fetch the daily news
    related to different topics.
    Go to : https://newsapi.org/
    and explore various options to build you application"""
    # api_key = 763c2ab6a08b499589a0f04352203d98

import requests
import tkinter as tk



print("Please give general INFO about the NEWS you wanna read")
category = input("Category of the news\n(general ,business ,entertainment \n,health ,science ,sports ,technology) : ")

def getNews():
    api_key = "763c2ab6a08b499589a0f04352203d98"
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""
    
    for article in articles:
        my_articles.append(article["title"])
    
    for i in range(10):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n\n"
    
    print(my_news)

a = getNews()

# # The above program is desgnined to run in terminal if u want to run application then uncomment the downward code and comment out 'a = getNews()' 
# canvas = tk.TK()
# canvas.geometry("900x600")
# canvas.title("News App")

# button = tk.Button(canvas , font = 24 , text = "Reload" , command = getNews)
# button.pack(pady = 20)

# label = tk.Label(canvas , font = 18 , justify = "left")
# label.pack(pady = 20)

# canvas.mainloop()
