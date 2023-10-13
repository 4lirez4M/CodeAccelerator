import json

for i in range(1, 3):
    firstname, lastname, phone, email = input(
        "Enter the first and last name and "
        "Phone and email respectively with a space: ").split()
    Dic = {
        "firstname": firstname,
        "lastname": lastname,
        "Phone": phone,
        "email": email
    }
    filename = f"file{i}.json"
    with open(filename, "w") as outfile:
        json.dump(Dic, outfile, indent=2)
