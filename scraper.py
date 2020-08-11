import requests
from bs4 import BeautifulSoup
  
URL = "https://minecraft.gamepedia.com/Sword"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib')
# general area of HTML I want to parse
crafting = soup.find('table', recursive=True, attrs={'data-description': 'Crafting recipes'})
test = crafting.find('tbody').find_all('tr')
print(test[1].find('td').text.strip())

# crafting recipe 9 block structure
recipe = crafting.find('span', attrs={'class': 'mcui-input'})

# get a basic structure of how the recipe looks
# TODO: need to fine tune what the ingredients actually are
for row in recipe.children:
    # print(row)
    for item in row:
        # print(item.find('span'))
        out = item.find_all('a')
        if len(out) != 0:
            print(out[-1]['title'])
        else:
            print(out)
        # skip empty item slot case; no <a> tag
        # if out is not None:
        #     print(out['href'])
        # else:
        #     print(out)
    print('+--------+')

# maybe in the future return some json object? probably work well with JS bot
