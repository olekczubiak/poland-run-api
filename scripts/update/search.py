from bs4 import BeautifulSoup

##for run-log.com
time = []
name = []
distance = []
place = []
website = []


def open_file(filename):
    with open(filename, 'r') as f:
        read_file = f.read()
        return read_file

def append_to_list(list_name, variable):
    for element in variable:
        if list_name == name:
            list_name.append(element.text.replace("\n", ""))
        else:
            list_name.append(element.text.replace("\n", "").replace(" ", ""))

def append_events(example):
    soup = BeautifulSoup(open_file(example), "html.parser")
    finder_01 = soup.find_all("tr", {"class": "vevent row even"})
    finder_02 = soup.find_all("tr", {"class": "vevent row odd"})
    for element_01, element_02 in zip(finder_01, finder_02):
        append_to_list(time, element_01.find_all("td", {"class": "dtstart"}))
        append_to_list(name, element_01.find_all("a", {"class": "url summary"}))
        append_to_list(distance, element_01.find_all("td", {"class": "distance"}))
        for a in element_01.find_all("a", href=True):
            website_addr = 'https://run-log.com/' + a['href']
            # append_to_list(website, website_addr)
            website.append(website_addr)
        append_to_list(place, element_01.find_all("td", {"class": "location"}))

        append_to_list(time, element_02.find_all("td", {"class": "dtstart"}))
        append_to_list(name, element_02.find_all("a", {"class": "url summary"}))
        append_to_list(distance, element_02.find_all("td", {"class": "distance"}))
        for a in element_02.find_all("a", href=True):
            website_addr = 'https://run-log.com/' + a['href']
            website.append(website_addr)
        append_to_list(place, element_02.find_all("td", {"class": "location"}))