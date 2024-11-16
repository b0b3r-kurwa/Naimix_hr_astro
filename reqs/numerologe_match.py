import requests

from transliterate import translit
import json


def num_match(name1:str,dob1:str,name2:str,dob2:str):

    name1 = translit(name1,'ru',reversed=True)
    name2 = translit(name2, 'ru', reversed=True)

    import requests

    url = "https://numerology-match-making.p.rapidapi.com/MatchMaking"

    querystring = {"your_name": name1, "your_dob": dob1, "partner_name": name2,
                   "partner_dob": dob2}

    headers = {
        "x-rapidapi-key": "7147666237msh746130e931165ebp1b7430jsnfb564298dc53",
        "x-rapidapi-host": "numerology-match-making.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    js = response.json()




name1, dob1,name2,dob2 = map(str,input().split())

num_match(name1, dob1,name2,dob2)

# матвей 2005-02-15 дмитрий 2004-11-10