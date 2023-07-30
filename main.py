from requests import get
from bs4 import BeautifulSoup

base_Url = 'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term='
search_term = 'python'

response = get(f"{base_Url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for posts in job_posts:
            print(posts)
            print("//////////")