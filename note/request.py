import requests

url = "https://doctorgpt.p.rapidapi.com/doctorgpt"

querystring = {"condition":"diabetes","specialist":"true"}

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "doctorgpt.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
