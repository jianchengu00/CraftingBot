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
  You need to generate your own Discord API key and add it **config.json** like such:  
  ```
  {   
      "prefix": "$",  
      "token": "Your_Discord_API_Key"     
  } 
  ```
    
  Primary commands are written in Python, and they need to be hosted by a local Flask API to be callable by JavaScript. First start server like so:   
  `$ python python_api.py`
  
  Since the JS bot is already configured to localhost, it will be able to reach the Flask API endpoints, so simply start the bot:  
  `$ node index.js`
  
