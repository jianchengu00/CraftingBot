from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import pprint


app = Flask(__name__)


# function called when specified endpoint is reached, and will scrape the Minecraft Wiki
@app.route('/functions/description', methods=['GET'])
def find_description():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    if 'item_name' in request.args:
        verbose = False
        item_name_elements = str(request.args['item_name']).split('_')
        # if verbose is part of the arguments sent in the GET request,
        # then set it as True and remove it from the list of strings
        if '--verbose' in item_name_elements:
            verbose = True
            item_name_elements.remove('--verbose')
        # reconstruct the item name string (which should not have '--verbose') in any case
        item_name = '_'.join(item_name_elements)
    else:
        # If no ID is provided, return an empty JSON response
        return jsonify({})

    # item description as dictionary representation
    description = {}

    # construct URL to item in question
    url = f"https://minecraft.gamepedia.com/{item_name}"
    # open website with requests
    r = requests.get(url)
    # generate Soup object w/ HTML content
    minecraft_wiki_soup = BeautifulSoup(r.content, 'html5lib')

    # high level part of HTML tree of where I can parse the recipe
    description_soup = minecraft_wiki_soup.find('div', recursive=True, attrs={'id': 'mw-content-text'})
    # get the description located in the first <p> tag of the description soup
    if verbose:
        for idx, p in enumerate(description_soup.div.div.find_next_siblings('p')):
            skip_strings = ['Java Edition', 'Bedrock Edition']
            if not any(x in p.get_text(' ', strip=True) for x in skip_strings):
                description[str(idx)] = p.get_text(' ', strip=True)
    else:
        description["text"] = description_soup.div.div.find_next_siblings('p')[0].get_text(' ', strip=True)

    # return as JSON via HTTP GET request to the Discord bot
    return jsonify(description)


# function called when specified endpoint is reached, and will scrape the Minecraft Wiki
# page to find an item's recipe
@app.route('/functions/recipe', methods=['GET'])
def find_recipe():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    if 'item_name' in request.args:
        item_name = str(request.args['item_name'])
    else:
        # If no ID is provided, return an empty JSON response
        return jsonify({})

    # recipe with description + 9 block structure as dictionary representation
    recipe = {}

    # construct URL to item in question
    url = f"https://minecraft.gamepedia.com/{item_name}"
    # open website with requests
    r = requests.get(url)
    # generate Soup object w/ HTML content
    minecraft_wiki_soup = BeautifulSoup(r.content, 'html5lib')

    # high level part of HTML tree of where I can parse the recipe
    crafting_soup = minecraft_wiki_soup.find('table', recursive=True, attrs={'data-description': 'Crafting recipes'})

    # find and add item crafting description as a data point to be returned, which are in the first <tbody> tag
    # and include all the <tr> tags inside the <tbody>
    crafting_description = crafting_soup.find('tbody').find_all('tr')
    # get the second <tr> tag inside the crafting_description and get the first <td> tag,
    # which contains the recipe's description
    # strip all whitespace and rejoin with a single whitespace for uniformity, then split by distinct recipe items
    recipe_text = crafting_description[1].find('td').get_text(' ', strip=True).split(' + ')
    # add quotes to each distinct recipe item in a recipe for more user clarity
    recipe_text_formatted = [f'\"{text}\"' for text in recipe_text]
    recipe['description'] = ' + '.join(recipe_text_formatted)

    # get soup object of crafting recipe's 9 block structure, which are located at the first <span> tag with
    # attribute 'class': 'mcui-input'
    recipe_soup = crafting_soup.find('span', attrs={'class': 'mcui-input'})

    # get a basic structure of how the recipe looks
    for row_num, row in enumerate(recipe_soup.children):
        # create a new row for each crafting row in the HTML representation
        recipe[str(row_num)] = {}
        for item_num, item in enumerate(row):
            # get all <a> tags which occur for each item in a row
            out = item.find_all('a')
            if len(out) != 0:
                recipe[str(row_num)][str(item_num)] = f"[{out[0]['title']}]"
            else:
                # empty tag/no item in this slot
                recipe[str(row_num)][str(item_num)] = "[]"

    # return as JSON via HTTP GET request to the Discord bot
    return jsonify(recipe)


if __name__ == '__main__':
    app.run(debug=True)
