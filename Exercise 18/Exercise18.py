import os
import json

employees = [
    {
        'name': 'ali',
        'lastname': 'alizadeh',
        'personal ID': 1780,
        'national ID': 1290856,
        'Date': '2020/20/20',
        'type': 'Programming',
        'salary': 120000
    },
    {
            'name': 'reza',
            'lastname': 'ramezani',
            'personal ID': 1850,
            'national ID': 1265456,
            'Date': '2020/20/22',
            'type': 'Programming',
            'salary': 100000
        },
    {
                'name': 'mani',
                'lastname': 'mohamadi',
                'personal ID': 1932,
                'national ID': 1260854,
                'Date': '2020/20/24',
                'type': 'security',
                'salary': 140000
            }
]
os.mkdir('Programming')
os.mkdir('security')
for item in employees:
    filename = f"./{item['type']}/{item['name']}/{item['name']}.json"
    if item['type'] == "Programming":
        os.mkdir(f"./Programming/{item['name']}")
        with open(filename, "w") as f:
            json.dump(item, f, indent=2)

    else:
        os.mkdir(f"./security/{item['name']}")
        with open(filename, "w") as f:
            json.dump(item, f, indent=2)


