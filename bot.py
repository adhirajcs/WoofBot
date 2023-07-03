# Import the necessary modules
import discord as dc
import responses as res
import APIs_keys_url as aku



# Define an asynchronous function to send a message to the user
async def send_message(message, user_message, is_private):
    try:
        response = res.get_response(user_message)
        
        if is_private:
            await message.author.send(response)
        
        else:
            await message.channel.send(response)
        
    except Exception as e:
        print(e)


# Define the function to run the Discord bot
def run_discord_bot():
    TOKEN = aku.token
    intents = dc.Intents.default()
    intents.message_content = True
    client = dc.Client(intents=intents)


    # Define an event handler for when the bot is ready and connected to the server
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!!!")
    
    # Define an event handler for when a message is received
    @client.event
    async def on_message(message):

        # Ignore messages sent by the bot itself to prevent infinite loops
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Print the user's message and channel for debugging purposes
        print(f'{username} said: "{user_message}" ({channel})')

        # Check if the user's message starts with a question mark '?'
        if user_message[0] == '?':

            # Remove the question mark from the message
            user_message = user_message[1:]

            # Send the user's message as a private response
            await send_message(message, user_message, is_private=True)

        else:
            # Send the user's message as a public response
            await send_message(message, user_message, is_private=False)

    # Run the bot with the provided token
    client.run(TOKEN)