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
                '-- <bot currently under development>\n\n' +
                'Commands:\n' +
                '\trecipe     -- Prints a diagram of a Minecraft item\'s recipe\n' +
                '\tgreet      -- Mentions all users listed with \"What\'s up!\"\n' +
                '\tserver     -- Prints the server information\n' +
                '\tuser-info  -- Prints user information of whoever entered the command```';
