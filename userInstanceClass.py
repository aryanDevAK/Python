class Member:
    def __init__(self,username,fullName):
        self.username=username
        self.fullName=fullName

guy1 = Member("Gugu","Ruhi Sharma")
guy2 = Member("Kaku","Aryan Khatri")

print(guy1)
print(guy1.fullName)
print(guy1.username)
print(type(guy1))

print(guy2)
print(guy2.fullName)
print(guy2.username)
print(type(guy2))

service = "free"
conditionValue = "You have paid for the service." if service == "paid" else "Please pay for the service."
print(conditionValue)