module.exports = {
	name: 'greet',
    description: 'Greet Users Listed',
    guildOnly: true,
    args: true,
    usage: '<user> ... <user>',
	execute(message, args) {
        // check # of mentions
        if (!message.mentions.users.size) {
            message.reply('You need to tag users in order to get a response from me!');
        } else if (message.mentions.users.size > 5) {
            message.reply('More than 5 users tagged. Pls limit to <= 5 to avoid to minimize spamming!');
        } 

        // build a list of replies, based on # of users mentioned
        const replyList = message.mentions.users.map(user => {
            return `What's up <@${user.id}> !`;
        });
        message.channel.send(replyList);
	},
};