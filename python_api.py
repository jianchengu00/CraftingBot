from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

# TODO: maybe add another function to provide description about a Minecraft item


@app.route('/functions/recipe', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'item_name' in request.args:
        item_name = str(request.args['item_name'])
    else:
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

    # find and add item crafting description as a data point to be returned
    crafting_description = crafting_soup.find('tbody').find_all('tr')
    # strip all whitespace and rejoin with a single whitespace for uniformity, then split by distinct recipe items
    recipe_text = crafting_description[1].find('td').get_text(' ', strip=True).split(' + ')
    # add quotes to each distinct recipe item in a recipe for more user clarity
    recipe_text_formatted = [f'\"{text}\"' for text in recipe_text]
    recipe['description'] = ' + '.join(recipe_text_formatted)

    # get soup object of crafting recipe's 9 block structure
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
