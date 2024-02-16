## Process for scraper

1) Get the url, store as a variable - in time, it should be able to read from a list, i.e. for each list of urls, scrape all the events
2) Using BS4 to parse the HTML and Selenium to interact with the JS on the page. In this case, Selenium uses *.click()* 
to:
    - Render the anchor link for the same url
    - wait for page to load (can test to see if elements are loaded and using *wait*)
    - scrape all elements on the page - *Title*, *Date*, *Event*
3) Results are in tabular format, so:
    - The *time* column needs to be checked for any **DNS** values - if those are in a list, then the last elements of all the other columns need to be removed. The alternative is to do it when the data is in the pandas dataframe. 

4) Column Headings:
    - Place
    - Lane
    - Bib
    - Name
    - Category
    - Team (only valid for XC results)
    - Club
    - Result
    - Info

*Result* will show whether an athlete has a DNS and can therefore be removed from the results.


## Things to explore:
- Currently, hand-coding the total number of athletes. Whilst ok for testing, this is unfeasible long-term as the total amounts of athletes can 
never be known. What is known however, is the total amount of columns, so any list can be divided by that number to find the athletes

## Friday to-do:
- Upload diagram
- Add to README and upload
- Programmatically create folder(s) for Event and Event/category/images

## to-do:
- ~~Draw a diagram - this will help plan~~
- get a list of lists, then:
- auto-slice the list and perform checking - Not feasible to hand-code for athletes as numbers vary
- figure out how to add to CSV


## Longer-term:
- try/catch blocks for error checking
    - Page title/date
- save all images to a seperate folder
- save CSV's in a seperate folder by category title - get this from BS4
- seperate CSV for:
    - Middle Distance
    - Jumps
    - Throws
    - Sprints
- Investigate putting into MySQL database
- Get the participants from the main anchor page and use that to slice up list




References:
1) [How to split a list into equal-sized chunks](https://www.python-engineer.com/posts/split_list_in_chunks/)<br>
2)