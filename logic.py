from bs4 import BeautifulSoup
import requests
import re

#
def get_insta_link_info(pagelink, switch):
    try:
        r  = requests.get(pagelink)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    if switch == 'text':
        data = r.text
    elif switch == 'bits':
        data = r.content
    else:
        print('No such function')

    return data


def get_insta_pic(pagelink):

    # getting data from specific page
    data = get_insta_link_info(pagelink, 'text')
    # pattern for extracting main picture link
    pattern = '\"display_url\": \"(http://|https://)\S+jpg'
    # getting useful part of text
    ref = re.finditer(pattern, data)

    name = input('Enter picture name: ')

    # patter of unnecessary part
    pat = '\"display_url\": \"'

    # iterating through all found patterns
    for k, i in enumerate(ref):
        a = i.group(0)
        # getting rid if unnecessary part
        link = a.replace(pat, '')
        # making request to pic url
        req = requests.get(link)

        # saving pic to pc
        with open(name+'.jpg', 'wb') as pic:
            pic.write(req.content)


def get_insta_text(pagelink):
    switch = 'text'
    #switch = 'bits'
    data = get_insta_link_info(pagelink, switch)
    print(data)


def get_youtube_video(pagelink):
    #switch = 'text'
    switch = 'bits'
    data = get_insta_link_info(pagelink, switch)
    #print(data)
    soup = BeautifulSoup(data, 'lxml')

    lk = soup.find_all('a')

    for i in lk:
        a = i.find_all('href')
    print(a)


if __name__ == '__main__':
    #"https://www.instagram.com/usachevruslan/?hl=ru"
    link = 'https://www.instagram.com/p/BVVb0CiAlVj/?taken-by=usachevruslan&hl=ru'
    #link = "https://www.instagram.com/p/BVVPLnwAqn9/?taken-by=usachevruslan&hl=ru"
    #link = 'https://www.youtube.com/watch?v=a6wJxjePPCA'
    get_insta_pic(link)
    #get_youtube_video(link)
    #get_insta_text(link)
