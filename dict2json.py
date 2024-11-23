import json

Q_dict = [
{
    "id":1,
    "Q":'what is your name?'
},
{
    "id":2,
    "Q":'what is your favourite food?'
},
{
    "id":3,
    "Q":'what is your age?'
},
{
    "id":4,
    "Q":'who is your favourite actor?'
},
{
    "id":5,
    "Q":'what is your favourite season?'
},
{
    "id":6,
    "Q":'what is your favourite subject?'
}
]

with open('test.json','w') as f:
    json.dump(Q_dict,f)