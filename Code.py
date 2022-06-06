from bs4 import BeautifulSoup
import requests
import smtplib


def n12():
    link = "https://www.n12.co.il/"
    source = requests.get(link).text
    soup = BeautifulSoup(source , 'lxml')
    id = soup.find(id = "part1")
    place = 0
    arr = []
    arr.append('N12 : ')
    for i in range(1 , 19 , 3):
        try:
            headline = id.find_all('a')[i].text + " " + id.find_all('a')[i+1].text
            place = place + 1
        except:
            pass
        arr.append(str(place)+"." +headline)
    arr.append(f'Link to the website : {link}')
    arr.append(" ")
    arr.append(" ")
    hey = '\n'.join(arr)

    return hey


def weather():
    link = "https://www.ynet.co.il/weather"
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    weather = soup.select_one('div.forcast-tempature-mobile').text + f'Link to the website : {link}'
    return weather


def bbc():
    link ='https://www.bbc.com/'
    source = requests.get(link).text
    soup = BeautifulSoup(source , 'lxml')
    media = soup.find('ul' , class_ = 'media-list')
    headline = media.find_all('li' , class_= 'media-list__item')
    arr = []
    j = 2
    arr.append('BBC : ')
    arr.append("1." + headline[0].a.text.strip() + ' ' + headline[0].p.text.strip())
    for i  in range(1,5):
        arr.append(str(j) + "." + headline[i].a.text.strip())
        j=j+1
    arr.append(f'Link to the website : {link}')
    hey = '\n'.join(arr)
    return hey


def mariv():
    link = 'https://www.maariv.co.il/'
    arr = []
    source = requests.get(link).text
    soup = BeautifulSoup(source , 'lxml')
    top = "1." +soup.select_one('div.top-story-text-wrap').find_all('span')[1].text.strip() + " " +soup.select_one('div.top-story-text-wrap').find_all('span')[2].text
    article = soup.select("div.three-articles-in-row-text-wrap")
    arr.append('Mariv : ')
    arr.append(top)
    j=2
    for i in range(0,2):
        arr.append(str(j)+"."+article[i].find(class_ = "three-articles-in-row-overlay-text").text.strip() + article[i].find(class_ = "three-articles-in-row-title title-hover draft-title-cms").text.strip())
        j=j+1
    arr.append(f'Link to the website : {link}')
    hey = '\n'.join(arr)
    return hey


articles_array = ['The weather is : ' + weather() , " "," ", "Hey, it's Mike the NewsBot here is your news for today,\nHave a great day! " ," ", n12() , bbc() ,' ',' ',  mariv()]
message = '\n'.join(articles_array).encode('utf-8')
sender_email = 'amit.gilat5@gmail.com'
rec_email = 'amit.gilat5@gmail.com'
password = 'xinmcjuukjkqnruw'
server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login(sender_email , password)
server.sendmail(sender_email , rec_email , message)
