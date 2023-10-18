stores = {
    1: {
        "Title": "shop 1",
        "shop category": "clothing",
        "economical number": "123"
    },
    2: {
        "Title": "shop 2",
        "shop category": "shoes",
        "economical number": "234"
    },
    3: {
        "Title": "shop 3",
        "shop category": "clothing",
        "economical number": "345"
    },
    4: {
        "Title": "shop 4",
        "shop category": "bags",
        "economical number": "456"
    },
    5: {
        "Title": "shop 5",
        "shop category": "shoes",
        "economical number": "567"
    },
    6: {
            "Title": "shop 6",
            "shop category": "clothing",
            "economical number": "678"
    }
}
dic = {"clothing": [], "shoes": [], "bags": []}
for item in stores:
    if stores[item]["shop category"] == "clothing":
        dic['clothing'].append(stores[item]["Title"])
    elif stores[item]["shop category"] == "shoes":
        dic['shoes'].append(stores[item]["Title"])
    elif stores[item]["shop category"] == "bags":
        dic['bags'].append(stores[item]["Title"])
print(dic)



