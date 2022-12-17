import os
from content.wwr import extract_wwr_jobs
from content.indeed import extract_indeed_jobs

os.system("clear")

print("\n검색어를 입력하시오:\n")
keyword = input().rstrip()

wwr = extract_wwr_jobs(keyword)
indeed = extract_indeed_jobs(keyword)

jobs = wwr + indeed

print("\n", "---- 검 색 결 과 ----")
for job in jobs:
    print(job, "\n")

print("\n", f"{keyword} 직업을 모두 {len(jobs)}개 발견되었습니다.")
