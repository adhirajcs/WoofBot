# WoofBot

WoofBot is a Discord bot created using Python 3.11.3 that provides various commands to enhance your Discord server experience, including:

- Greeting users

- Rolling dice

- Getting quotes

- Getting facts about Chuck Norris

- Getting weather reports

- Getting help

- Getting information about the creator

- Listing all of the commands

## Table of Contents

- [Commands](#commands)
- [APIs](#apis)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Author](#Author)

## Commands

WoofBot responds to the following commands:

1. `#hello`: Greet the bot and receive a warm welcome.
2. `#roll`: Roll a dice and get a random number between 1 and 6.
3. `#quote`: Get an inspirational quote.
4. `#fact` or `#facts`: Get a random fact about Chuck Norris.
5. `#weather (city name)`: Get the weather report of a specified city.
6. `#help`: Display the help menu with available commands and their usage.
7. `#creator`: Get information about the creator of the bot.
8. `#commands`: Display a list of all available commands.

To receive responses in direct messages (DMs), prefix the command with `?#`. For example, `?#hello` will send the greeting message to your DM instead of the channel.

## APIs

WoofBot utilizes the following APIs to provide certain commands:

- [zenquotes.io](https://zenquotes.io/api/random): Provides random quotes for the `#quote` command.
- [api.chucknorris.io](https://api.chucknorris.io/jokes/random): Fetches random facts about Chuck Norris for the `#fact` command.
- [api.openweathermap.org](https://api.openweathermap.org/data/2.5/weather?q={city}&appid={aku.openWeatherApi}): Retrieves weather data for the `#weather` command. Note that you need to replace `{city}` with the desired city name and `{aku.openWeatherApi}` with your OpenWeather API key.

Make sure to obtain your own API key and replace the placeholder `{aku.openWeatherApi}` with your actual API key in the weather API URL.

## Installation

To set up WoofBot on your own server, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/woofbot.git`
2. Install the required dependencies: `pip install discord` and `pip install requests`
3. Set up the required environment variables:
   - `DISCORD_TOKEN`: Your Discord bot token
   - `OPENWEATHER_API_KEY`: Your OpenWeather API key
4. Start the bot: `python bot.py`

Note: Ensure you have Python 3.6 or higher installed on your system.

## Usage

Once the bot is running and added to your server, you can start using the commands in any text channel.

To interact with WoofBot, simply type the desired command in a text channel. For example, typing `#hello` will trigger the greeting message. Remember to prefix the command with `?#` if you want to receive the response in DM.

Feel free to explore all the available commands and make the most out of WoofBot!

## Contributing

Contributions to WoofBot are welcome! If you have any ideas, suggestions, or bug reports, please open an issue on the [GitHub repository](https://github.com/your-username/woofbot) or submit a pull request with your changes.

## License

WoofBot is not licensed. Therefore you are free to use it.

## Bibliography/Reference

- [The EASIEST Discord Chat Bot Tutorial On The Internet (Python 3.10) 2023](https://youtu.be/1yLfjMtsV9s) by [Indently](https://www.youtube.com/@Indently) - This YouTube tutorial served as the foundational resource for building my WoofBot.

## Author

[Adhiraj Saha](https://github.com/adhirajcs)
