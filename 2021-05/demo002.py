import json

d = {
    'a': 'a',
    'b': True,
    'c': False,
    'd': None
}
print(json.dumps(d))

print(json.loads('{"a": "a", "b": true, "c": false, "d": null}'))
