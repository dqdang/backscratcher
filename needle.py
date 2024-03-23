import argparse
import json
import os
import requests
from string import Template
import sys
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
                        username = account.split("#")[0]
                        tag = account.split("#")[1]
                        all_sites.append(s.substitute(user=username, tag=tag))
    return all_sites


def only_gg(names):
    all_sites = []
    op_gg = "https://na.op.gg/summoner/userName=$user$tag"
    for name in names.keys():
        for account in names[name]:
            s = Template(op_gg)
            all_sites.append(s.substitute(user=account))
    return all_sites


def open_sites_in_browser(sites):
    try:
        if sys.platform == 'win32':
            browser = webbrowser.get('windows-default')
        elif sys.platform == 'darwin':
            browser = webbrowser.get('macos')
        else:
            browser = webbrowser.get('mozilla')
    except Exception as e:
        print(e)
        return
    browser.open(sites[0], new=1)
    if len(sites) > 1:
        for site in sites[1:]:
            browser.open_new_tab(site)


def make_parser():
    parser = argparse.ArgumentParser(description="open sites from sites.txt for all summoners in summoners.json")
    parser.add_argument("--opgg", dest="opgg", action='store_true')
    return parser


def main():
    names = get_summoner_names()
    parser = make_parser()
    args = parser.parse_args()
    if args.opgg:
        sites = only_gg(names)
    else:
        sites = grab_sites(names)
    open_sites_in_browser(sites)


if __name__ == "__main__":
    main()
