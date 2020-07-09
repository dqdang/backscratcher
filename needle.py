import json
import requests
from string import Template
import webbrowser


def get_summoner_names():
    with open("summoner.json") as f:
        names = json.load(f)
        return names


def grab_sites(names):
    all_sites = []
    with open("sites.txt") as f:
        sites = f.readlines()
        for name in names.keys():
            for account in names[name]:
                for i in range(len(sites)):
                    if sites[i] != "\n":
                        s = Template(sites[i])
                        all_sites.append(s.substitute(user=account))
    return all_sites


def open_sites_in_browser(sites):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
    browser = webbrowser.get(chrome_path)
    for site in sites:
        browser.open_new(site)


def main():
    names = get_summoner_names()
    sites = grab_sites(names)
    open_sites_in_browser(sites)


if __name__ == "__main__":
    main()
