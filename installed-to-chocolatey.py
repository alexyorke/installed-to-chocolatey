import winreg
import requests 
import feedparser
import urllib.parse
import sys

# https://stackoverflow.com/questions/53132434/list-of-installed-programs
def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)
names_and_feeds = {}
for software in software_list:
    if ('Update for ' in software['name'] or '(remove only)' in software['name']):
        continue
    url = "https://chocolatey.org/api/v2/Search()?$filter=IsLatestVersion&$skip=0&$top=2&searchTerm=" + urllib.parse.quote("'" + software['name'] + "'") + "&targetFramework=%27%27&includePrerelease=false"
    d = feedparser.parse(url)
    if (len(d['entries']) > 0 and 'title' in d['entries'][0]):
        names_and_feeds[software['name']] = {"name": d['entries'][0]['title'], "version": software['version']}
    else:
        # remove the last word and re-do the search
        software['name'] = software['name'].rsplit(' ', 1)[0]
        url = "https://chocolatey.org/api/v2/Search()?$filter=IsLatestVersion&$skip=0&$top=2&searchTerm=" + urllib.parse.quote("'" + software['name'] + "'") + "&targetFramework=%27%27&includePrerelease=false"
        d = feedparser.parse(url)
        if (len(d['entries']) > 0 and 'title' in d['entries'][0]):
            names_and_feeds[software['name']] = {"name": d['entries'][0]['title'], "version": software['version']}
    
print("﻿<?xml version=\"1.0\" encoding=\"utf-8\"?><packages>")
for software in list(set(names_and_feeds.keys())):
    print("<package id=\"" + names_and_feeds[software]['name'] + "\" version=\"" + names_and_feeds[software]['version'] + "\" />")
print("</packages>")
sys.stderr.write("\n\n\nThis is how I matched them:")
for software in names_and_feeds.keys():
    sys.stderr.write(software + "->" + names_and_feeds[software]['name'] + "\n")
