from content.wwr import extract_wwr_jobs

print("\n검색어를 입력하시오:\n")
keyword = input().rstrip()

jobs = extract_wwr_jobs(keyword)
print(*jobs, sep="\n\n")
