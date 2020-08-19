const axios = require('axios');

module.exports = {
	name: 'description',
    description: 'Find item\'s description',
    guildOnly: true,
    args: true,
    cooldown: 5,
    usage: '<item> <name> <verbosity>',
	execute(message, args) {
	    // GET request to local Flask server to run Python backend function
	    axios({
            method: 'get',
            url: 'http://127.0.0.1:5000/functions/description',
            params: {
                item_name: args.join('_'),
            },
            responseType: 'json'
	    }).then(function (response) {
	        // get JSON response object
            let description_json = response.data;
            // print out item description
            for (let text in description_json) {
                if (description_json.hasOwnProperty(text)) {
                    message.channel.send(`\`\`\`${description_json[text]}\`\`\``);
                }
            }

        }).catch(function (error) {
             // handle error
            message.channel.send("There was an error involving this function");
            message.channel.send(error.toString());
      });
	}
};
