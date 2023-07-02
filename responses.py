import discord as dc
import random
import requests
import APIs_keys_url as aku


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
        return f"{quote}  ~{author}"
    

    elif p_message == "#fact" or p_message == "#facts":
        rs = requests.get("https://api.chucknorris.io/jokes/random")
        data = rs.json()
        return data["value"]
                            

    elif p_message.startswith("#weather"):
        city = p_message[8:]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={aku.openWeatherApi}"
        rs = requests.get(url)
        data = rs.json()
        temp = (data["main"]["temp"]) - 273.15
        icon = f'http://openweathermap.org/img/wn/{data["weather"][0]["icon"]}.png'
        
        return f'Temp: {temp:.{4}}°C \nDescription: {data["weather"][0]["description"]} \n{icon}'


    elif p_message == "#help":
        return "Sorry for your inconvenience, please contact my creator!!! or checkout the list of all commands using `#commands`."
    
    
    elif p_message == "#creator":
        return "The name of my creator is Adhiraj Saha. You can check for more details about him in his github page https://github.com/adhirajcs/."
    
    
    elif p_message == "#commands":
        return "Type `?#` before the Command to get response in DM. \nType `#hello` for greetings, \nType `#roll` to roll a dice, \nType `#quote` for a quote, \nType `#fact` or `#facts` for a fact about Chuck Norris, \nType `#weather (city name)` for weather report of a city, \nType `#help` for help, \nType `#creator` for creator's info, \nType `#commands` for list of commands."


    return