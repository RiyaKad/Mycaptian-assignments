#Project 2 : Web scraper using BeautifulSoup4 and requests
from bs4 import BeautifulSoup

import requests , openpyxl
excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Top Rated Movies'
print(excel.sheetnames)

sheet.append(['Movies Rank','Movies Name','Year of relase','IMDB rating'])
try:
    
     source = requests.get("https://www.imdb.com/chart/top")
#to capture error
     source.raise_for_status()
     
     soup = BeautifulSoup(source.text, "html.parser")
     
     movies = soup.find('tbody', class_="lister-list").find_all('tr')
     
     
     for movie in movies: 
         
    
          
          name = movie.find('td', class_="titlecolumn").a.text
          
          rank = movie.find('td', class_="titlecolumn").get_text(strip=True).split('.')[0]
          
          year = movie.find('td', class_="titlecolumn").span.text.strip('()')
          
          rating = movie.find('td',class_="ratingColumn imdbRating").stong.text

        
          


          print(rank,name,year,rating)
          sheet.append([rank,name,year,rating])
          
     
except Exception as e :
         print (e)
         
excel.save('IMDB Movie raing.xlsx')


