import json
import os.path

keys_internal = {}

def keys():
    global keys_internal
    if not keys_internal:
        try:
            with open('keys.json') as f:
                keys_internal = json.loads(f.read())
        except IOError as e:
            with open(os.path.expanduser('~/.config/nyt/keys.json')) as f:
                keys_internal = json.loads(f.read())
    return keys_internal
