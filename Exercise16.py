dic = {
    "ali alizadeh": {
        "Intelligence": 84,
        "General information": 60,
        "Information technology": 40,
    },

    "shahin khani": {
        "Intelligence": 90,
        "General information": 85,
        "Information technology": 70,

    },
    "reza ramezani": {
        "Intelligence": 70,
        "General information": 50,
        "Information technology": 30,

    }
}
grads = {}
for person, info in dic.items():
    grad = (info["Intelligence"] * 5 + info["General information"] * 3 +
            info["Information technology"] * 4)
    grads[person] = grad
print(grads)
a = 0
for key, value in grads.items():
    if value > a:
        a = value

print("The best candidate: ", list(grads.keys())[list(grads.values()).index(a)])





