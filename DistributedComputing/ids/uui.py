import uuid

myuuid = uuid.uuid4()
myuuidStr = str(myuuid)

sameMyUuid = uuid.UUID(myuuidStr)

print(sameMyUuid)
print(myuuidStr)
assert myuuid == sameMyUuid