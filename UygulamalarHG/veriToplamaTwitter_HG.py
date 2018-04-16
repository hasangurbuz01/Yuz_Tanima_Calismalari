from selenium import webdriver
from string import punctuation
from bs4 import BeautifulSoup

browser=webdriver.Chrome("/Users/hasangurbuz/Downloads/chromedriver")
browser.get('http://twitter.com/login')
class twitterGiris():
    browser.find_element_by_class_name('js-username-field').send_keys('hasan.gurbuz@windowslive.com')
    browser.find_element_by_class_name('js-password-field').send_keys('hg1976')
    browser.find_element_by_class_name('clearfix').submit()
    soup=BeautifulSoup(browser.page_source,'html.parser')
    tweets=[p.text for p in soup.findAll('p', class_='tweet-text')]
    print(tweets)
    noktalama=str.maketrans('','',punctuation)
    tweets=tweets.translate(noktalama)
    tweets=tweets.upper()
    tweet_say=Counter(tweets)
    print(type(tweet_say),'\n')
    for tweet in tweet_say.most_common(30):
        print(tweet)