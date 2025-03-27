# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. 
# Käytä seuravalla sivulla esiteltävää 
# rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import my_requests

pyyntö = "https://api.chucknorris.io/jokes/random"
try:
    vastaus = my_requests.get(pyyntö)

    if vastaus.status_code == 200:  
        joke = vastaus.json()['value']  
        print(joke)
    else:
        print("Virhe: Vitsiä ei voitu hakea.")

except Exception as e:
    print("Haku epäonnistui:", str(e))





