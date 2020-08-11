// TODO: IDEAS
/*
    Scraping the web for minecraft recipes?
    Maybe print out the general ingredients and then a generated text image of
    ingredient placements
*/


// require Node's file system module
const fs = require('fs');
// require config file to get API key
const { prefix, token } = require('./config.json');
// require the discord.js module
const Discord = require('discord.js');

// create a new Discord client
const client = new Discord.Client();
// create a Collection to store the commands from the *.js command files
client.commands = new Discord.Collection();

// dynamically fetch all command files
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

// add all the commands form command file to the command collection above
for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	// set a new item in the Collection
	// with the key as the command name and the value as the exported module
	client.commands.set(command.name, command);
}

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
    client.user.setActivity('Don\'t mind me, I\'m still under development');
});

// when the client sees a new message, run this code
// will trigger on any new message
client.on('message', message => {
    // ignore if message doesn't start with "$cb" or message was sent by another bot
    if (!message.content.startsWith(`${prefix}`) || message.author.bot) return;

    // parse message as an array of args, use regex to avoid spaces causing bugs
    const args = message.content.trim().split(/ +/);

    // remove and store the bot name elem
    const botName = args.shift().toLowerCase();

    // check if no bot commands were provided
    // if no bot commands were provided, then args should be expected to be empty, 
    // as the bot name elem (also the only elem) was removed from args
    if (!args.length && botName === `${prefix}`) {
        message.channel.send('Asking me for a command? Type \"$cb help\" for more information');
        return;
    } 

    // remove and store the bot's command elem
    const commandName = args.shift().toLowerCase();

    // ignore if command doesn't exist
    if (!client.commands.has(commandName)) {
        message.channel.send('CraftingBot doesn\'t know this command! Type \"$cb help\" for more information');
        return;
    }

    // fetch the command from the command Collection we populated earlier
    const command = client.commands.get(commandName);

    // check if command is server/guild + text channel ONLY
    if (command.guildOnly && message.channel.type !== 'text') {
        return message.reply('I can\'t execute that command inside DMs!');
    }

    // check if this specific command requires arguments, and if yes, if there there >= 1 args provided
    if (command.args && !args.length) {
        let reply = `You didn't provide any arguments, ${message.author}!`;
        // check if the command.js file has a specific usage format
		if (command.usage) {
			reply += `\nThe proper usage would be: \`${prefix} ${command.name} ${command.usage}\``;
		}
		return message.channel.send(reply);
    }

    // handle commands
    try {
        command.execute(message, args);
    } catch (error) {
        message.reply('There was an error trying to execute that command!');
    }

});

// login to Discord with your app's token
client.login(token);
