import http.client

conn = http.client.HTTPSConnection("linkedin-data-scraper.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "0681a179d5msh89e94fb285b0f63p1053a0jsn069280ca84cf",
    'x-rapidapi-host': "linkedin-data-scraper.p.rapidapi.com"
}

conn.request("GET", "/profile_updates_original?profile_url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fingmar-klein&page=1&reposts=1&comments=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))