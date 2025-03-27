"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä
paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan
API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi."""


import json
import my_requests


api_key = "	API TK"


kaupunki = input("Anna paikkakunnan nimi: ")


url = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"

try:
    
    vastaus = my_requests.get(url)
    
    if vastaus.status_code == 200:
       
        data = vastaus.json()
        
       
        lämpötila = data['main']['temp']
        lämpötila_celsius = lämpötila - 273.15  
        säätila = data['weather'][0]['description']
        tuuli = data['wind']['speed']
        nimi = data['name']

        
        print(f"Kaupunki: {nimi}")
        print(f"Lämpötila: {lämpötila_celsius:.1f} °C")
        print(f"Sää: {säätila}")
        print(f"Tuuli: {tuuli} m/s")
    else:
        print("Virhe: Säätietoja ei voitu hakea. Tarkista paikkakunnan nimi ja API-avain.")
except Exception as e:
    print("Haku epäonnistui:", str(e))
