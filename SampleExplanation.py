



# --------------REQ SKILLS --- COMPANY NAME ---------------



from bs4 import BeautifulSoup
import requests
import times

#-------Filteration part-------------Do this part atlast
def find_job():
    print("Post some skills that you are not familiar")
    unmatched_skill = input('>') #------>get input from the user
    print(f'Filtering out {unmatched_skill}')

#link of the website
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text.strip()
    skills = job.find('span', class_='srp-skills').text.strip()
    published_date = job.find('span', class_="sim-posted").span.text.strip()
    info = job.header.h2.a['href']
    print(f"Company Name : {company_name.strip()}")
    print(f"Required skills : {skills.strip()}")
    print(f"Info : {info.strip()}")
    
 
    print('')

    # print(f"Company Name : {company_name.strip()}")
    #         print(f"Required skills : {skills.strip()}")

# Instead of use f''',   use print(f" separately to ensure proper alignment.
    

#this part for execute the code every 10 seconds like an updation------
#-------Do this part at last
if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        times.sleep(time_wait * 60)


