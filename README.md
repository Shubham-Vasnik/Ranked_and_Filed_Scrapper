# Ranked and Filed Scrapper 
### by Shubham Vasnik

# Steps To Use The App 

## For Linux 
 Step 1 : Navigate to the directory where the files are stored note that 'run_scrapper.sh' and  'scrapper.py' must be in the same directory.

 Step 2 : Open the terminal in that directory and run command **'./run_scrapper.sh'** to run the scrapper. Running this command will ask for your password as it requires su permissions. This Command will run a script which will install the requirements to run the scrapper and the run the scrapper.

 This Command might  take around 5 minutes to run (time may vary based on your computer specs and internet connection) after the command is finshed running the scrapped data is stored in **'data.json'** file 

## For Windows 

 Step 1 : Navigate to the folder where the files are stored note that 'run_scrapper.sh' and  'scrapper.py' must be in the same folder.

 Step 2 : Open the cmd in that folder and run command **'pip install requests tqdm'** (for this command to work you must have python and pip installed on your computer) . This Command will install the dependencies to run the scrapper.py file 

 Step 3 : Then run **'python scrapper.py'** command to run the scraper.

 This Command might  take around 5 minutes to run (time may vary based on your computer specs and internet connection) after the command is finshed running the scrapped data is stored in **'data.json'** file 

# Working 

 Instead of using selenium I used pythons built-in requests package as the 'rankandfiled.com' is a infinite scrolling website scraping it with selenium will require to scroll the entire page to load all the contents which is a slow process. As infinite scrolling websites makes ajax request to fetch the new data we can use this requests to scrape  the data.

