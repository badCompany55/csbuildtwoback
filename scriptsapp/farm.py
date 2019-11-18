import requests
import time
import json
import random
# import os
import getopt, sys
# from dotenv import load_dotenv

all_command_args = sys.argv
arg_list = all_command_args[1:]
unixOptions = "k:h"
gnuOptions = ["key=", "help"]


try:
    args, values = getopt.getopt(arg_list, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    sys.exit(x)

for curr_arg, curr_val in args:
    if curr_arg in ("-k", "--key"):
        key = curr_val


def load():
    with open("scriptsapp/final-path-graph.json", "r") as f:
        return json.load(f)

def load_find_path():
    with open("scriptsapp/pathgraph.json", "r") as f:
        return json.load(f)

# load_dotenv()

# key = os.getenv("KEY")

find_path_graph = load_find_path()


final_path_graph = load()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"
api_url = "http://127.0.0.1:8000/api/"


auth_header = {"Authorization": f"Token {key}"}

reverse = {"n": "s", "s": "n", "e": "w", "w": "e"}


def init():
    response = requests.get(f"{base_url}init/", headers=auth_header)
    start = response.json()
    # print(start)
    time.sleep(start["cooldown"])

    return start


def move(direction, room):
    response = requests.post(
        f"{base_url}move/",
        json={"direction": direction, "next_room_id": f"{room}"},
        headers=auth_header,
    )
    new_room = response.json()
    for message in new_room["messages"]:
        print(message)
    print(f'You can move in {new_room["cooldown"]} seconds')
    time.sleep(new_room["cooldown"])

    return new_room


def status():
    response = requests.post(f"{base_url}status/", headers=auth_header)
    stats = response.json()
    time.sleep(stats["cooldown"])

    return stats


def loot(item):
    response = requests.post(
        f"{base_url}take/", json={"name": item}, headers=auth_header
    )
    treasure = response.json()
    print(treasure["messages"][0])
    time.sleep(treasure["cooldown"])


def drop(item):
    response = requests.post(
        f"{base_url}drop/", json={"name": item}, headers=auth_header
    )
    treasure = response.json()
    print(treasure["messages"][0])
    time.sleep(treasure["cooldown"])


def sell(item):
    response = requests.post(
        f"{base_url}sell/", json={"name": item, "confirm": "yes"}, headers=auth_header
    )
    treasure = response.json()
    print(treasure["messages"][1])
    time.sleep(treasure["cooldown"])

def find_path(start, destination):

    q = Queue()
    q.enqueue([start])

    visited = []
    while q.size() > 0:
        current_path = q.dequeue()
        current_room = current_path[-1]

        if current_room == destination:
            return current_path

        if current_room not in visited:
            visited.append(current_room)
            possible_directions = [
                key for key, value in find_path_graph[str(current_room)].items() if value != "?"
            ]

            for direction in possible_directions:
                copy_path = current_path[:]
                next_room = find_path_graph[str(current_room)][direction]
                copy_path.append(next_room)
                q.enqueue(copy_path)

stats = status()
while stats["gold"] < 1000:
    start = init()

    end = random.randint(300, 499)
    route = find_path(start["room_id"], end)
    print(route)
    for i in range(len(route) - 1):
        cur_room_id = route[i]
        next_room_id = route[i + 1]
        key = []
        step = [
            key for key, value in final_path_graph[0][str(cur_room_id)].items() if value == next_room_id
        ]
        new_room = move(step[0], next_room_id)

        for treasure in new_room["items"]:
            if stats["encumbrance"] == stats["strength"]:
                break
            loot(treasure)
            stats = status()

        if stats["encumbrance"] == stats["strength"]:
            break

    start = init()
    route = find_path(start["room_id"], 1)
    print("Returning!")
    print(route)

    for i in range(len(route) - 1):
        cur_room_id = route[i]
        next_room_id = route[i + 1]
        step = [
            key
            for key, value in final_path_graph[0][str(cur_room_id)].items()
            if value == next_room_id
        ]
        new_room = move(step[0], next_room_id)

    for treasure in stats["inventory"]:
        sell(treasure)

    stats = status()

print(f'Done! You have {stats["gold"]} gold')
# for message in new_room["messages"]:
#     print(message)
# print(f'You can move in {new_room["cooldown"]} seconds')

# time.sleep(new_room["cooldown"])








