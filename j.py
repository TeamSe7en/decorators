import json
def decorate_to_json(func):
    def wrapper():
        print(func())
        if isinstance(func(), dict):
          print(json.dumps(func(),sort_keys = True))
        else:
         print(func())
    return wrapper

@decorate_to_json
def diction():
    return {5:"a",2:"b",1:"c"}

@decorate_to_json
def number():
    return [1,2,3]

diction()
number()