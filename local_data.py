import random
import os
import discord

def get_advice():
    advice_list = [
        "Siempre apaga las luces cuando no las estés usando.",
        "Recicla y reutiliza plásticos o cartones siempre que sea posible.",
        "Utiliza bicicletas o transporte público en lugar de autos para reducir la contaminación.",
        "Cuidar la naturaleza es responsabilidad de todos, recuerdales.",
        "Tener un huerto en casa ayuda a reducir la huella de carbono y a tener alimentos frescos.",
    ]
    return random.choice(advice_list)

def get_visual():
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
    fl = os.listdir(image_dir)
    choice = random.choice(fl)
    with open(os.path.join(image_dir, choice), 'rb') as f:   
        picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
    return picture

def get_page():
    page_list = [
        "https://www.wwf.org.co/que_hacemos/",
        "https://www.greenpeace.org/colombia/",
        "https://www.nationalgeographic.com/environment/article/10-ways-to-help-the-environment",
        "https://www.un.org/sustainabledevelopment/",
        "https://www.epa.gov/students",
    ]
    return random.choice(page_list)
