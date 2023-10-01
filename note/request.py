import requests

url = "https://doctorgpt.p.rapidapi.com/doctorgpt"

querystring = {"condition":"diabetes","specialist":"true"}

headers = {
	"X-RapidAPI-Key": "49e3e5866fmshe7319c653c8a4fdp1d1721jsne467a20e9e73",
	"X-RapidAPI-Host": "doctorgpt.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())