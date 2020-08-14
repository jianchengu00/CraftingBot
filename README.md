# CraftingBot
## Requires: 
  * Node.js w/ version v12.x.x
    * discord.js
    * axios
    * fs
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
    
  Some commands are written in Python, and they need to be called via a localhost Flask API. First set up this server like so:   
  **$** python python_api.py
  
  Since the JS bot is already configured to localhost, then just start it like so:  
  **$** node index.js
  
