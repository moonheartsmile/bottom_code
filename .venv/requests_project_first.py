import requests


params = {'q' : 'Perm', 'appid' : 'token', 'units' : 'metric'}

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

x = response.json()

print(x['weather'][0]['main'])
#print(response.status_code)
#print(response.headers)
print(response.text)
print(response.json())

