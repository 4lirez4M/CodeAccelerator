dic = {
    1: {
        "Title": "",
        "bill": 12000,
        "discount": 5
    },
    2: {
            "Title": "",
            "bill": 14000,
            "discount": 2
        },
    3: {
            "Title": "",
            "bill": 16000,
            "discount": 3
        },
    4: {
            "Title": "",
            "bill": 20000,
            "discount": 6
        },
    5: {
            "Title": "",
            "bill": 130000,
            "discount": 7
        },
    6: {
            "Title": "",
            "bill": 200000,
            "discount": 10
        },
    7: {
            "Title": "",
            "bill": 280000,
            "discount": 12
        },
    8: {
            "Title": "",
            "bill": 100000,
            "discount": 5
        },
    9: {
            "Title": "",
            "bill": 80000,
            "discount": 6
        },
    10: {
            "Title": "",
            "bill": 900000,
            "discount": 20
        }
}
bills = 0
discounts = 0
for item in dic:
    bills += dic[item]["bill"]
    discounts += dic[item]["bill"] * (dic[item]["discount"] / 100)
print(f"Total cost: {bills}")
print(f"Total discount: {discounts}")
print(f"Total cost after discount: {bills - discounts}")
