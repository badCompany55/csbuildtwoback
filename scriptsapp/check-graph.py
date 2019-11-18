import json


def load_graph():
    with open("path-graph.json", "r") as f:
        return json.load(f)


def load_names():
    with open("room-names.json", "r") as f:
        return json.load(f)


path_graph = load_graph()

print(len(path_graph))


names = load_names()

important_names = [
    (key, value) for key, value in names.items() if value != "A misty room"
]

if len(path_graph) == 500:
    with open("final-path-graph.json", "w") as f:
        json.dump((path_graph, important_names), f)

for name in important_names:
    print(name[0], name[1])
