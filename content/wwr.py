import requests
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    search_term = "python"

    response = requests.get(f"{base_url}{search_term}")
    if response.status_code != 200:
        print("해당 사이트를 Request하는데 실패하였습니다.")
        return

    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")
    for job in jobs:
        posts = job.find_all("li")[:-1]
        for post in posts:
            anchor = post.find_all("a")[1]
            position = post.find("span", class_="title")
            link = anchor["href"]
            company, _, location = anchor.find_all("span", class_="company")
            job_data = {
                "link": f"https://weworkremotely.com{link}",
                "company": company.string,
                "location": location.string,
                "position": position.string,
            }
            results.append(job_data)
    return results
