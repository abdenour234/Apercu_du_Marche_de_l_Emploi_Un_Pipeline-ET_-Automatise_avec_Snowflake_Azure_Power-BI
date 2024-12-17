import requests

url = "https://linkedin-data-scraper.p.rapidapi.com/search_jobs"

payload = {
	"keywords": "Data scientist",
	"location": "morocco",
	"count": 50
}
headers = {
	"x-rapidapi-key": "7bbaa81c63msh190363b3189eb05p10f6d2jsne405b9c1ded2",
	"x-rapidapi-host": "linkedin-data-scraper.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())