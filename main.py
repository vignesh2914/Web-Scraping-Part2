from bs4 import BeautifulSoup
import requests
import time  # Corrected import statement

# Function for job search and filtering
def find_job():
    print("Post some skills that you are not familiar")
    unmatched_skill = input('>')  # Get input from the user
    print(f'Filtering out {unmatched_skill}')

    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        published_date = job.find('span', class_="sim-posted").span.text.strip()
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            info = job.header.h2.a['href']

            if unmatched_skill not in skills:
                print(f"Company Name : {company_name.strip()}")
                print(f"Required skills : {skills.strip()}")
                print(f"Info : {info.strip()}")
                print('')

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'waiting for {time_wait} minutes...')
        time.sleep(time_wait * 60)
