from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews = GoogleNews(period='7d')
googlenews.search(input("Enter Country Name: "))
result = googlenews.result()
for x in result:
    print("-"*50)
    print("Title--",x['title'])
    print("Date/Time--",x['date'])
    print("Description--",x['desc'])
    print("Link--",x['link'])