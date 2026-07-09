# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# List to store all scraped books
all_books = []

# Loop through all pages
for page in range(1,51):
    # Determine URL based on page number
    if page==1:
        url = "http://books.toscrape.com/"
    else:
        url =f"http://books.toscrape.com/catalogue/page-{page}.html"
        
        # Send request and parse HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    

    # Find all books on current page 
    books = soup.find_all("article")
    
    # Extract details from each books
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_ = "price_color").text.replace("Â","")
        rating = book.find("p", class_ = "star-rating")["class"][1]
        availablity = book.find("p", class_ = "instock availability").text.strip()
        book_data = {
            "Title":title,
            "Price" : price,
            "Rating" : rating,
            "Availability" : availablity
        
        }
        all_books.append(book_data)
    
df = pd.DataFrame(all_books)
print(df)
df.to_csv("output/books.csv",index=False, encoding="utf-8-sig")