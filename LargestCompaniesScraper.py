import bs4
import pandas as pd 
import requests

# when scraping over the internet
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

#when scraping a local file
# with open("Companies.htm", 'rb') as fp:
# 	soup = bs4.BeautifulSoup(fp, features="lxml")

companies = soup.find_all('tbody')[0].find_all('tr')

data = []
for company in companies[2:]:
	data.append([
		company.find_all('td')[0].get_text().rstrip(),
		company.find_all('td')[1].get_text().rstrip(),
		company.find_all('td')[2].get_text().rstrip(),
		company.find_all('td')[3].get_text().rstrip(),
		company.find_all('td')[4].get_text().rstrip(),
		company.find_all('td')[5].get_text().rstrip()
	])
	
companies_df = pd.DataFrame(data, columns=["Name","Industry","Revenue","Profit","Employees","Country"])

print('10 Largest companies in the world by revenues:')
print(companies_df)

# # Save data
# writer = pd.ExcelWriter('LargestCompanies.xlsx')
# companies_df.to_excel(writer,'Largest Companies')
# writer.save()








