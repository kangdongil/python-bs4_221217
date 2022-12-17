import math
from selenium import webdriver
from config.options import options
from bs4 import BeautifulSoup


def get_total_pages(soup, limit):
    try:
        job_count_response = soup.find(
            "div", class_="jobsearch-JobCountAndSortPane-jobCount"
        ).text
        job_total = int(job_count_response.split()[1][:-1].replace(",", ""))
        page_total = math.ceil(job_total / limit)
        if page_total > 10:
            page_total = 10
        print("\n", f"{format(job_total, ',')}개를 발견하였습니다.")
        return page_total
    except AttributeError:
        print("\n", "검색 결과를 찾지 못했습니다.")
        return 0


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
            "link": f"https://kr.indeed.com{link}",
            "company": company.string.replace(",", " "),
            "location": location.string.replace(",", " "),
            "position": position.string.replace(",", " "),
        }
        results.append(job_data)
    return results


def extract_indeed_jobs(keyword):

    base_url = "https://kr.indeed.com/jobs"
    limit = 50
    results = []

    browser = webdriver.Chrome(options=options)
    browser.get(f"{base_url}?q={keyword}")
    print("\n", f"Indeed에서 {keyword} 직업 검색을 시작합니다..", "\n")
    soup = BeautifulSoup(browser.page_source, "html.parser")

    page_total = get_total_pages(soup, limit)

    if page_total == 0:
        return []

    for page in range(page_total):
        request_url = f"{base_url}?q={keyword}&limit={limit}&start={page*limit}"
        print(f"요청중... {request_url}")

        browser.get(request_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        result = parse_job_data(soup)
        results += result

    return results
