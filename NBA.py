from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re
import pymysql

#This function grabs the url and returns and returns the BeautifulSoup object
def getSoupFromURL(url):
    try:
        r = requests.get(url)
    except:
        return None
    return BeautifulSoup(r.text, "html.parser")

#This function 
def getgamelogurl(player_url):
    overview_soup = getSoupFromURL(player_url)
    gamelog_url_list = list()
    for li in overview_soup.find_all('li'):
        game_log_links = []
        if 'Game Logs' in li.getText():
            game_log_links =  li.findAll('a')
        for game_log_link in game_log_links:
            if 'gamelog' in game_log_link.get('href'):
                gamelog_url_list.append('http://www.basketball-reference.com' + game_log_link.get('href'))
    return set(gamelog_url_list)

def readfile(filename):
    player_url_list = list()
    openedfile = open(filename, 'r')
    for line in openedfile:
        player_url_list.append("http" + line.split("http")[1].strip())
    return player_url_list

def main():
    player_url_list = readfile('Active_Player.txt')
    for url in player_url_list:
        print(getgamelogurl(url))
main()