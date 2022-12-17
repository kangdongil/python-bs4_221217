from selenium import webdriver
from config.options import options
from bs4 import BeautifulSoup


def parse_job_data(soup):
    results = []

    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all("li", recursive=False)
    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone is not None:
            continue
        anchor = job.select_one("h2 a", class_="jobTitle")
        position = job.find("h2", class_="jobTitle")
        link = anchor["href"]
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            "link": f"https://kr.indeed.com/{link}",
            "company": company.string,
            "location": location.string,
            "position": position.string,
        }
        results.append(job_data)
    return results


def extract_indeed_jobs():
    base_url = "https://kr.indeed.com/jobs"
    keyword = "python"

    browser = webdriver.Chrome(options=options)
    browser.get(f"{base_url}?q={keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")

    results = parse_job_data(soup)
    for result in results:
        print(result, "\n")


extract_indeed_jobs()
