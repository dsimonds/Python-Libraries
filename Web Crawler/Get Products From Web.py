import requests
from bs4 import BeautifulSoup

# gets product names from category page and writes to csv file.
# pass to function category url, and total pages to crawl
def divers_direct(web_page, max_pages):
    page = 1
    # creates file, names it with url.com/x/file-name
    file_name = (web_page.rsplit('/', 1)[-1]).replace("?p=", '')
    f = open(file_name + '.csv', 'w+')
    f.write('Product Name\n')
	# crawls through pages
    while page <= max_pages:
        url = web_page + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
		# loops through all instances of elements of class : className
        for link in soup.findAll('h2', {'class': 'product-name'}):
            print(link.string)
            f.write(link.string + '\n')
        page += 1
    f.close()

# assign url, add pagination variable
url = 'http://www.diversdirect.com/scuba-diving/diving-accessories/dry-bag-case'
url += '?p='
divers_direct(url, 15)
