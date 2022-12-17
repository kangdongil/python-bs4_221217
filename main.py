import os
from content.wwr import extract_wwr_jobs
from content.indeed import extract_indeed_jobs

os.system("clear")

print("\n검색어를 입력하시오:\n")
keyword = input().rstrip()


wwr = extract_wwr_jobs(keyword)
indeed = extract_indeed_jobs(keyword)
jobs = wwr + indeed

file = open(f"{keyword}.csv", "w")
file.write("POSITION,COMPANY,LOCATION,LINK\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
