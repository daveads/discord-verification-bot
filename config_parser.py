from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


with open("bot_config.toml", "rb") as f:
    data = tomllib.load(f)


#print(type(data))
#print(data)
print(data['channels_id'])

print(data['channels_id']['self_verification'])


for i in data['channels_id']:
    #print(i)
    ""


"""
for i in data:
    #print(i)
    pprint(data[i])
"""
#print("**parsaing**")
