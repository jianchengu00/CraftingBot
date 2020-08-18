const axios = require('axios');

module.exports = {
	name: 'recipe',
    description: 'Find item\'s recipe',
    guildOnly: true,
    args: true,
    cooldown: 5,
    usage: '<item> <name>',
	execute(message, args) {
	    // GET request to local Flask server to run Python backend function
	    axios({
            method: 'get',
            url: 'http://127.0.0.1:5000/functions/recipe',
            params: {
                item_name: args.join('_'),
            },
            responseType: 'json'
	    }).then(function (response) {
	        // get JSON response object
            let recipe_json = response.data;
            // print out crafting description
            message.channel.send(recipe_json["description"]);
            // print out prettified crafting structure from JSON
            let reply = '```';
            for (let row in recipe_json) {
                if (recipe_json.hasOwnProperty(row)) {
                    if (row !== "description") {
                        for (let item in recipe_json[row]) {
                            if (recipe_json[row].hasOwnProperty(item)) {
                                reply += recipe_json[row][item] + ' ';
                            }
                        }
                        reply += '\n'
                    }
                }
            }
            reply += '```';
            message.channel.send(reply);

        }).catch(function (error) {
             // handle error
            message.channel.send("There was an error involving this function");
            message.channel.send(error.toString());
      });
	}
};
