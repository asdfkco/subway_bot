from datetime import datetime

now = datetime.now()

if(now.hour >= 0 and now.hour < 6):
    print("막차끊김")
else:
    print("열여있다")