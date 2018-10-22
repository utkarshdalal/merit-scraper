# merit-scraper
A python script to scrape real-time energy mix data from www.meritindia.in and store it to a csv file

## Step-by-step tutorial

1. Open the terminal. `cd` into the folder where you want to keep the script, then clone this repo by entering `git clone https://github.com/utkarshdalal/merit-scraper.git`

2. Install the BeautifulSoup library by entering `pip install BeautifulSoup4` in the terminal.

3. To have this file run on a schedule, we will have to configure it as a cron job. The following steps describe how to do this.

4. Let's assume we want the job to run every 15 minutes, and that we have saved the script to the path /path/to/file/merit-scraper.py.

5. Open crontab by entering `crontab -e` in the terminal.

6. Add the line `*/15 * * * * python /path/to/file/merit-scraper.py` to the crontab.

7. The job should now run, and you will see results added in /path/to/file/meritindia_data.csv.

8. You should also see logging in /path/to/file/meritindia_data.log when the script runs and when it finishes.

## Caveats

1. Note that this script is written in python 2.7. It should be compatible with python 3 but has not been tested.

2. This script relies on the format of www.meritindia.in not changing. If the order the values are in changes, the existing csv file 
will be moved to a file called {current_timestamp}meritindia_data.csv and a new file will be created with a new header row. An error 
will also be logged to /path/to/file/meritindia_data.log.

3. The first column of the CSV file is the timestamp that the script was run at. It is in UTC timezone. 
