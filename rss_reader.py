import requests  # pulling data
from bs4 import BeautifulSoup  # xml parsing
import json  # exporting to files


# save function
def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)


# scraping function
def desafora2_rss():
    article_list = []

    try:
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://desafora2.libsyn.com/rss')
        soup = BeautifulSoup(r.content, features='xml')

        # select only the "items" I want from the data
        articles = soup.findAll('item')

        # for each "item" I want, parse it into a list
        for a in articles:
            try:
                title = a.find('title').text
                link = a.find('link').text
                published = a.find('pubDate').text

                try:
                    image = a.find('image')["href"]
                    description = a.find('subtitle').text
                    url = a.find('enclosure')["url"]
                except Exception as e:
                    print('Error al cargar URL / imagen:')
                    print(a.find('title').text)
                    print(e)

                # create an "article" object with the data
                # from each "item"
                article = {
                    'title': title,
                    'link': link,
                    'published': published,
                    'image' : image,
                    'description' : description,
                    'url' : url,
                }

                # append my "article_list" with each "article" object
                article_list.append(article)

            except Exception as e:
                print('The scraping job failed. See exception:')
                print(a.find('title').text)
                print(e)

        # after the loop, dump my saved objects into a .txt file
        return article_list
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
