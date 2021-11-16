import requests
import os
from selenium import webdriver
import bs4

# new, top, mix, tracj and artits urls
top_url = "http://soundcloud.com/charts/top"
new_url = "http://soundcloud.com/charts/new"
track_url = "http://soundcloud.com/search/sounds?q="
artists_url = "http://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"

#create the selenium browser
browser = webdriver.Chrome("C:\\Users\\Joao\Desktop\\Proggraming\\SoundScrape\\chromedriver.exe")
browser.get("https://soundcloud.com")

# main menu
print("\n\Bem vindo ao Sound Scraper do Python!")
print("\nExplore os Top Charts de todos os gêneros, pesquise por musicas, artistas e playlists!")

while True:
    print("Menu")
    print("1. Search for a track")
    print("2. Search for an artist")
    print("3. Search for a mix")
    print("4. Top charts")
    print("5. New & Hot Charts")

    choice = int(input("Select: "))
    
    #quit browser
    if choice == 0:
        browser.quit()
        break
    print()

    # search for a track
    if choice == 1:
        name = input("Name of the track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)

    #search for an artist
    if choice == 2:
        name = input("Name of the artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artists_url + name)

    #search for a mix
    if choice == 3:
        name = input("Name of the mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(mix_url_end + name)

