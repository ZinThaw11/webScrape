from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.bbc.com/burmese/topics/cl3rq8rkqgxt?page="
total_pages = 6
news_list = []

for page in range(1, total_pages + 1):
    new_url = url + str(page)
    response = requests.get(new_url)

    # Ensure the response content is decoded using the correct encoding
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    news_parents = soup.find_all('li', class_='bbc-t44f9r')  # Updated to match the list items
    print(len(news_parents))


    for parent in news_parents:
        # Find the title
        news_anchor = parent.find('a')
        news_title = news_anchor.text.strip() if news_anchor else 'No title'
        
        # Find the date
        news_date = parent.find('time')
        news_date_text = news_date.text.strip() if news_date else 'No date'
        
        news_list.append({'title': news_title, 'date': news_date_text})
        print(f"Title: {news_title}, Date: {news_date_text}")

# Create a DataFrame
df = pd.DataFrame(news_list)
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_excel('news_titles_and_dates.xlsx', index=False)