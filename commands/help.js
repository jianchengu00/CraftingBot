module.exports = {
	name: 'help',
    description: 'Help Menu',
    guildOnly: true,
    args: false,
	execute(message, args) {

        message.channel.send(helpMessage);
	},
};

helpMessage = '```$craft\n\n' +
                '-- I\'m a bot that fetches you Minecraft item & crafting info!\n\n' +
                'Commands:\n' +
                '\trecipe       -- Prints a diagram of the Minecraft item\'s recipe\n' +
                '\tdescription  -- Prints Wiki description of the Minecraft item\n' +
                '\t                  Add the \'--verbose\' flag as the last arg for more info!\n' +
                '\tgreet        -- Mentions all users listed with \"What\'s up!\"\n' +
                '\tserver       -- Prints the server information\n' +
                '\tuser-info    -- Prints user information of whoever entered the command```';
