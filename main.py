import requests
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = requests.get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("해당 사이트를 Request하는데 실패하였습니다.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all("section", class_="jobs"))
