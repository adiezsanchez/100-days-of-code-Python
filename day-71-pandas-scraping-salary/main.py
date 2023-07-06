from bs4 import BeautifulSoup
import requests
import pandas as pd

list_of_dicts = []

page = 1
while page < 35:

    url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    degree_soup = soup.select(selector=".data-table__value")

    scraped_list = []
    for major in degree_soup:
        scraped_list.append(major.getText())

    #print(scraped_list)
    cycles = len(scraped_list)

    n = 0
    for i in range (int(cycles / 6)):
        data_dict = {"Major": scraped_list[n + 1],
                     "Degree_Type": scraped_list[n + 2],
                     "Early_Career_Pay": int(scraped_list[n + 3].replace("$","").replace(",","")),
                     "Mid-Career_Pay": int(scraped_list[n + 4].replace("$","").replace(",",""))
        }
        list_of_dicts.append(data_dict)
        n += 6


    print(f"Page: {page}")
    print(f"List length: {len(list_of_dicts)}")
    page += 1

#print(f"Page: {page}")
#print(f"List length: {len(list_of_dicts)}")
#print(list_of_dicts)

df = pd.DataFrame(list_of_dicts)
print(df.head())

df.to_csv("college_salary_report.csv")