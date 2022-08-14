import requests
city=input("Pls enter city name:  ")
url = "https://api.openweathermap.org/data/2.5/weather?q= "+city+" &appid=84829329f9b843684e925058a1358ff1"


api_response = requests.get(url)
data = api_response.json()
print(api_response.text)
