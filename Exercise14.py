users = {
    1: {
        "firstname": "Ali",
        "lastname": "alizadeh",
        "status": True,
        "email": ""
    },
    2: {
            "firstname": "reza",
            "lastname": "ramezani",
            "status": False,
            "email": ""
        },
    3: {
            "firstname": "mani",
            "lastname": "abdoli",
            "status": True,
            "email": ""
        },
    4: {
            "firstname": "hamed",
            "lastname": "hamedzadeh",
            "status": True,
            "email": ""
        }
}
active = 0
inactive = 0
for item in users:
    if users[item]["status"] is True:
        active += 1
    else:
        inactive += 1
print(f"number of active users: {active}\nnumber of inactive users: {inactive}")
