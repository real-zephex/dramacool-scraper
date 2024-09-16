import re
import requests
from bs4 import BeautifulSoup

class Recent:
	def __init__(self) -> None:
		self.url = "https://asianc.to/recently-added"
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
			'Referer': "https://dramacool.com.pa/",
			'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
		}
		self.data = {
			"page": "popular",
			"status": None,
			"error": None,
			"results": []
		}
  
	def fetch_data(self):
		try:
			self.response = requests.get(self.url, headers=self.headers)
			self.data["status"] = self.response.status_code
			self.response.raise_for_status()
		except Exception as e:
			self.data["error"] = str(e)
			return self.data

		return (self.popular_parser())
	
	def popular_parser(self):
		soup = BeautifulSoup(self.response.content, "html.parser")
		cards = soup.find_all("a", class_="img")
		for item in cards:
			entry = {}
			entry["title"] = item.find("h3").get_text()
			entry["image"] = item.find("img", class_="lazy")["data-original"]
			entry["id"] = "/drama-detail/" + re.sub(r'-\d+$', '', entry["image"].split("/")[-1].split(".png")[0])

			self.data["results"].append(entry)

		return self.data
