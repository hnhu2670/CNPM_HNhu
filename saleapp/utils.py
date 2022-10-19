import json

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def read_cate():
    return read_json('data/categories.json')

