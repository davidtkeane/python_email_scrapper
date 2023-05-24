# python_email_scrapper
# Domain Email Scraper

The script will scrape the domain, save the email addresses to email_list.csv, and play a notification sound.

This Python script scrapes a single domain and returns a list of email addresses to the `email_list.csv` file. It also returns the domain searched addresses to the `url_search.csv` file. All searches will be saved in the files mentioned above.

The script uses BeautifulSoup to parse HTML and extract links and email addresses. It also uses simpleaudio to play a notification sound when the scraping is done.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

pip install -r requirements.txt

Usage

Open the script in a text editor. I am uisng Visual Studio on Windows 11. 
Replace the domain variable with the URL of the domain you want to scrape.
If desired, replace the audio_path variable with the path to a .wav file on your system.
Run the script: python script.py

Note: Each time you run the script for a new domain, you'll need to change the domain name in the script. I have added ATTENTION to where you have to change the two things.

There are two changes you need to make.
A. Replace the domain variable with the URL of the domain you want to scrape.
B. Replace the audio_path variable with the path to a .wav file on your computer

Note
This script was made using Visual Code and tested, this way we can see the folders, the code and the terminal making it easy to play with.
