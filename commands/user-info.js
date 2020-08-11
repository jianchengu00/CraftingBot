module.exports = {
	name: 'user-info',
    description: 'User Info',
    guildOnly: true,
    args: false,
	execute(message, args) {
		message.channel.send(`Your username: ${message.author.username}\nYour ID: ${message.author.id}`);
	},
};