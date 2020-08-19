# CraftingBot
## Requires: 
  * Node.js w/ version v12.x.x
    * discord.js
    * axios
    * jquery
  * Python 3.3+
    * Flask
    * BeautifulSoup4
    * Requests

## How to Run:
  **Important!!**   
  My Discord API key and bot prefix are stored in a local **config.json** file, which is intentionally gitignored from this repo for security.
  $CraftingBot is configured to use the **$craft** prefix  
  You need to generate your own Discord API key as well as set your own prefix if you'd like, then add them **config.json** like such:  
  ```
  {   
      "prefix": "$craft",  
      "token": "Your_Discord_API_Key"     
  } 
  ```
    
  Primary commands are written in Python, and they need to be hosted by a local Flask Web API to be callable by JavaScript. First start server:   
  `$ python api.py`
  
  Since the JS bot is already configured to localhost, it will be able to reach our Flask API endpoints, so simply start the bot:  
  `$ node index.js`
  
## Photo Demo
### Help Command
<img width="776" alt="Screen Shot 2020-08-18 at 7 07 57 PM" src="https://user-images.githubusercontent.com/25871150/90587575-8fa85200-e18e-11ea-8202-2833dcb6f5c7.png">

### Recipe Command
<img width="752" alt="Screen Shot 2020-08-18 at 3 51 07 PM" src="https://user-images.githubusercontent.com/25871150/90587486-57087880-e18e-11ea-81c9-778cc107f68f.png">

### Description Command
* Default
<img width="756" alt="Screen Shot 2020-08-18 at 7 08 31 PM" src="https://user-images.githubusercontent.com/25871150/90587651-be262d00-e18e-11ea-8ce3-302fc8b86670.png">

* Verbose
<img width="776" alt="Screen Shot 2020-08-18 at 7 09 06 PM" src="https://user-images.githubusercontent.com/25871150/90587663-c7af9500-e18e-11ea-8b2a-cf2c968f58c8.png">

