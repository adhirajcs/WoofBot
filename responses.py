import random
import requests


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "#hello":
        return "Hi! I am WoofBot ... woof woof 🐶!!!"
    
    elif p_message == "#roll":
        return str(random.randint(1,6))
    
    elif p_message == "#quote":
        rs = requests.get("https://zenquotes.io/api/random")
        quote = rs.json()[0]['q']
        author = rs.json()[0]['a']
        return f"{quote}  --{author}"

        

    elif p_message == "!help":
        return "Sorry for your inconvenience, please contact my creator!!! or checkout the list of all commands using `!commands`"
    
    elif p_message == "!creator":
        return "The name of my creator is Adhiraj Saha. You can check for more details about him in his github page https://github.com/adhirajcs/"
    
    elif p_message == "!commands":
        return "Type '?' before the Command to get response in DM. \nType `#hello` for greetings, \nType `#roll` to roll a dice, \nType `#quote` for a quote, \nType `!help` for help, \nType `!creator` for creator's info, \nType `!commands` for list of commands"
    

    return