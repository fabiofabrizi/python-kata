"""
This is the final version of the scraper.
Testing out new functionality can be found in different files

"""
############ Imports ####################################
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
# for folder creation
import os


############  Path & target url ##########################
path = "c:\\Users\\fabio\\Downloads"
#url = 'http://results.munsterathletics.com/2023/results_20230618/menu.html'
url = 'http://results.munsterathletics.com/2023/results_20230625/menu.html'

############  Set options ################################
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# set window size to native GUI size
option.add_argument("--window-size=1920,1080")  
option.add_argument("start-maximized")


############  Specify browser driver ######################
driver = webdriver.Chrome(options=option)

 
############  Getting page HTML through request parse content using BS4
driver.get(url) 
soup = BeautifulSoup(driver.page_source, 'html.parser') 

############ Screenshot of page ##########################
page_title = soup.select("title")
#print(f'page title is: {page_title[0].text}')
driver.save_screenshot(f'{page_title[0].text}.png')

############# Get the title of the competition: ##########
title_link = soup.select('#competition_name h2')
# print the title:
print(f'\nThis is the event title: {title_link[0].string}\n')

############# Create a folder and subfolder from title: ##########
title_list = (title_link[0].string).split(', ')
title = title_list[0]
title_date = title_list[-1]

path = (f'./{title}-{title_date}')
subpath = (f'./{title}-{title_date}/img')
# check whether directory already exists
if not os.path.exists(path):
  os.mkdir(path)
  print("Folder %s created!" % path)
else:
  print("Folder %s already exists" % path)

# check whether subdirectory exists
if not os.path.exists(subpath):
  os.mkdir(subpath)
  print("Folder %s created!" % subpath)
else:
  print("Folder %s already exists" % subpath)

############# Get a list of all events at competion: ################
all_title_links = soup.find_all('a', class_='menulink')
event_links = soup.find_all('a', class_='menueventlink')

# Get the events per group or category
events_per_group = soup.select('div#menu_results_table div.rounds')
all_title_links = all_title_links[1:-1]
print(f'Title links with Schedule and Textfile removed:\n{all_title_links}')
print(len(all_title_links))

# Create lists for grouped events and category titles
grouped_events = []
category_titles = []
# Event links
print("\nThese are all the event links")
#for event_link in event_links[:3]:
#    print(event_link.text)
print(f'Total number of events: {len(event_links)}')

# Event titles
print("\nThese are the event categories with \n'Schedule' and 'Results Textfile removed:\n")
for title in all_title_links:
    if (title.text != " Results Textfile") and (title.text != "Schedule"):
        #print(title.text)
        category_titles.append(title.text)
print(category_titles)

# Events grouped by category, i.e. middle distance, jumps, etc
#print("\nThis is the number of event categories:") 
for event in events_per_group:
    grouped_events.append(event)
print(f'\nThis is the number of categories: {(len(grouped_events))}')
#print(events_per_group)
index_events = len(grouped_events)
print(index_events)

# Make a list for the cleaned tags
cleaned_tags = []
##### Event extraction loop
print(f'\nThese are the cleaned links containing only anchor tags:\n')
#for index in range(len(events_per_group)):
for i in range(index_events):
    html_snippet = f'''{events_per_group[i]}'''
    # Parse the HTML snippet with BeautifulSoup
    soup2 = BeautifulSoup(html_snippet, 'html.parser')
    # Find all anchor tags within the div with class 'rounds'
    anchor_tags = soup2.select('.rounds a')
    # Double checking
    # print(len(anchor_tags))
    # Create a new list with the anchor tags
    new_list = [tag for tag in anchor_tags]
    
    # Append to the cleaned tags list
    cleaned_tags.append(new_list)
    # Print each element of the list    
    #print(new_list)
print(f'\nThis is the length of the list with cleaned tags: {len(cleaned_tags)}')
#for c in cleaned_tags:
#    print(f'\n{c}')
#print(f'This the amount of elements: {len(new_list)}')
#print(new_list)
##### End Event extraction loop

### To-do:
"""
- Make folder for title
- Make title/img/ folder to save images
- Test by looping through each category and 
   saving images of all events in that category
- 
"""