# This will scrape a single domain and return a list of email addresses to the email_list.csv file.
# Also returns the domain searched addresses to the url_search.csv file.
# All searches will be saved in the files mentioned above.
# pip install -r requirements.txt
# This script was made using Visual Code and tested, this way we can see the folders, the code and the terminal making it easy to play with.

import requests
import csv
import tempfile
import simpleaudio as sa
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from tqdm import tqdm
import os
from pydub import AudioSegment
from pydub.playback import play

# Define function to get all links on a page
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.add(href)
    return links

# Define function to extract email addresses from a page
def extract_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    email_addresses = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'mailto:' in href:
            email = href.split(':')[1].split('?')[0]
            email_addresses.add(email)
    return email_addresses

# Define domain to search 
# ATTENTION : This is where you enter the domain name in full path and include http:// 
# All you need to do is change the domain name every time you want to search.
domain = 'https://enter-domain-name-here.com'

# Get all links on the domain's home page
home_page_links = get_links(domain)

# Find the contact page link
contact_page_link = None
for link in home_page_links:
    if 'contact' in link.lower():
        contact_page_link = link
        break

# Scrape email addresses from the contact page, if it exists
if contact_page_link:
    contact_page_url = urljoin(domain, contact_page_link)
    contact_page_emails = extract_emails(contact_page_url)
else:
    contact_page_emails = set()

# Scrape email addresses from the rest of the domain
domain_emails = set()
for link in tqdm(home_page_links, desc='Scraping pages'):
    link_url = urljoin(domain, link)
    if urlparse(link_url).netloc == urlparse(domain).netloc:
        link_emails = extract_emails(link_url)
        domain_emails.update(link_emails)

# Write email addresses to a CSV file
with open('email_list.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for email in tqdm(contact_page_emails | domain_emails, desc='Writing to file'):
        writer.writerow([email])

# Write URL to url_search.csv file
with open('url_search.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([domain])


# Define the path to the audio file
# ATTENTION Change the wav file path and replace c:\Users\David\ to what system you want. Either Linux or Windows.
audio_path = r'C:\Users\David\git_domain_url_email_scrape\audio\youve-got-mail-sound.wav'

# Play audio notification
if os.path.exists(audio_path):
    wave_obj = sa.WaveObject.from_wave_file(audio_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()
else:
    print('Audio file not found!')

print(contact_page_emails | domain_emails)
