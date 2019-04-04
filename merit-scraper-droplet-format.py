import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import logging


def write_header():
    with open(csv_file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(column_headings)

# Change the following three lines to change where the file is stored
# Currently, it will store the file to the same directory where the script is located
# If you just want to change the name of the file, change the value of rel_path
script_dir = os.path.dirname('__file__')
rel_path = 'v1meritindia_data_nov21onwards.csv'
csv_file_path = os.path.join(script_dir, rel_path)

# Change the following line to change where logs will go to. Also change to change the log level.
logging.basicConfig(filename=os.path.join(script_dir, 'v1meritindia1_data_nov21onwards.log'), level=logging.INFO)

meritindia_url = 'http://www.meritindia.in'
current_datetime = datetime.utcnow().replace(microsecond=0).isoformat()
page = urllib.request.urlopen(meritindia_url)

html_content = BeautifulSoup(page, 'html.parser')

column_headings = ['TIMESTAMP']
row_values = [current_datetime]

file_exists = os.path.exists(csv_file_path)
header_matches = False

logging.info('Running merit-scraper.py at %s', current_datetime)

# Get data headers from website
data_types = html_content.find_all('div', 'gen_title_sec')
for data_type in data_types:
    column_headings.append(str(data_type.text.strip()))

# Get current data values from website
current_values = html_content.find_all('div', 'gen_value_sec')
for current_value in current_values:
    data_value = (current_value.find('span', 'counter'))
    row_values.append(data_value.text.strip().replace(',', ''))

# Create csv file and write header if it doesn't exist
if not file_exists:
    write_header()

# If headers have changed, rename existing file, log warning and create a new one with new headers
with open(csv_file_path, 'r') as f:
    header_matches = f.readline().strip().split(',') == column_headings
    if not header_matches:
        old_filename = os.path.join(script_dir, current_datetime + rel_path)
        os.rename(csv_file_path, old_filename)
        logging.warning('meritindia website layout changed! Created new csv file and renamed old one to %s',
                       old_filename)
        write_header()

# Add data row to csv
with open(csv_file_path, 'a') as f:
    cw = csv.writer(f)
    cw.writerow(row_values)

logging.info('merit-scraper.py run started at %s completed', current_datetime)