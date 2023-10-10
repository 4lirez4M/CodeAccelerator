from datetime import datetime
time = datetime.now().time()
secPass = time.hour * 3600 + time.minute * 60 + time.second
print(secPass)

