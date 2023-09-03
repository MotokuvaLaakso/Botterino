import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "!roll":
        return str(random.randint(0,10))
    
    if ", you just advanced to level" in p_message:
        return("https://tenor.com/view/lets-go-lets-goo-lest-gooooooooooooooooo-gif-19416648")
    
    else:
        return