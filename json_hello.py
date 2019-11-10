import json
data = '''{
    "name" : "ishita sharma",
    "phone" :{
        "type" : "intl",
        "number": "9467161455"

    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('name : ',info["name"])
print('Hide : ', info["email"]["hide"])