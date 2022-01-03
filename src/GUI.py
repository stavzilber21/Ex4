from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from GraphAlgo import GraphAlgo
from pygame import *

WIDTH, HEIGHT = 1080, 720
PORT = 6666
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

file = client.get_graph()



g = GraphAlgo()
g.load_from_json(file)
print(g)

pokemons = client.get_pokemons()
poke = g.load_pokemons(pokemons)
print(poke)

info = json.loads(client.get_info())
num_agents = info['GameServer']['agents']
for n in range(num_agents):
    name = "{\"id\":"+str(n)+"}"
    client.add_agent(name)


agents = client.get_agents()
agne = g.load_agents(agents)
print(agne)




