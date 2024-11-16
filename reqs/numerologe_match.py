import requests
import http.client
from transliterate import translit

def num_match(name1,dob1,name2,dob2):
    conn = http.client.HTTPSConnection("numerology-match-making.p.rapidapi.com")

    name1 = translit(name1,'ru',reversed=True)
    name2 = translit(name2, 'ru', reversed=True)

    headers = {
        'x-rapidapi-key': "7147666237msh746130e931165ebp1b7430jsnfb564298dc53",
        'x-rapidapi-host': "numerology-match-making.p.rapidapi.com"
    }

    conn.request("GET",
                 f"/MatchMaking?your_name={name1}&your_dob={dob1}&partner_name={name2}&partner_dob={dob2}",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


name1, dob1,name2,dob2 = map(str,input().split())
print(name1, dob1,name2,dob2)
num_match(name1, dob1,name2,dob2)