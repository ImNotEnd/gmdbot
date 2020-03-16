import requests
from json import loads

def everything():
    url = "https://corona.lmao.ninja/all"
    c = requests.get(url).text
    try:
        c1 = loads(c)
        x = f"There are currently {c1['cases']} global confirmed COVID-19 cases, {c1['deaths']} deaths and {c1['recovered']} recovered cases."
    except:
        x = f"Error fetching data. Server might be down."
    return x

def specific(country):
    url = f"https://corona.lmao.ninja/countries/{country}"
    c = requests.get(url).text
    try:
        c1 = loads(c)
        x = f"{c1['country']} currently has {c1['cases']} confirmed COVID-19 cases, {c1['deaths']} deaths and {c1['recovered']} recovered cases."
    except:
        x = f"Error fetching data. {country} might not exist"
    return x
