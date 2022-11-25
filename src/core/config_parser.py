from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib




"""
#print(type(data))
#print(data)
print(data['channels_id'])

print(data['channels_id']['self_verification'])


for i in data['channels_id']:
    #print(i)
    ""
"""


class BotConfigs:
    def __init__ (self):
        with open("bot_config.toml", "rb") as f:
            self.data = tomllib.load(f)
        
    def verfi_image(self):
        
        image = "img/" + self.data['image']['verfi_image']

        return image

