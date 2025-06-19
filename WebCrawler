import csv
from bs4 import BeautifulSoup
import requests

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    else:
        print("Failed to fetch HTML:", response.status_code)
        return None

def extract_movie_details(movie):
    title_element = movie.select_one('.ipc-title__text')
    title_text = title_element.get_text(strip=True) if title_element else None
    
    if title_text:
        index, title = title_text.split('.', 1)
    else:
        index, title = None, None
    
    year_element = movie.select_one('.cli-title-metadata-item')
    year = year_element.get_text(strip=True) if year_element else None
    
    rating_element = movie.select_one('.ipc-rating-star--imdb')
    rating = rating_element.get_text(strip=True) if rating_element else None
    
    return {"index": index.strip(), "title": title.strip(), "year": year, "rating": rating}

def scrape_imdb_top250(url):
    html = fetch_html(url)
    if html:
        movies = html.select('.ipc-metadata-list-summary-item')
        movie_details_list = []
        for movie in movies:
            movie_details = extract_movie_details(movie)
            if movie_details["title"]:
                movie_details_list.append(movie_details)
        return movie_details_list
    else:
        return None

def save_to_csv(movie_details, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Index', 'Title', 'Year', 'IMDb Rating', 'Review Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for movie in movie_details:
            rating_parts = movie['rating'].split('(')
            rating = rating_parts[0]
            review_count = rating_parts[1][:-1]
            
            writer.writerow({'Index': movie['index'], 'Title': movie['title'], 'Year': movie['year'], 'IMDb Rating': rating, 'Review Count': review_count})

url = 'http://www.imdb.com/chart/top'

top250_movies = scrape_imdb_top250(url)

csv_filename = 'imdb_top_250_movies.csv'

if top250_movies:
    for movie in top250_movies:
        print(f"Index: {movie['index']}, Title: {movie['title']}, Year: {movie['year']}, IMDb Rating: {movie['rating']}")
    
    save_to_csv(top250_movies, csv_filename)
    print(f"Scraped movie details saved to '{csv_filename}'")
else:
    print("Failed to scrape IMDb top 250 movies.")
