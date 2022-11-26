from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib




"""
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


    def guild_id(self):
        id = self.data['guild']['guild_id']
        return id

    
    def roles(self, role):

        if role == "self_ver":
            age_ver = self.data['roles']['self_ver']
            return age_ver
    


"""
see if it is possible to write directly into the .toml file
it should be possible tho

rather than using a txt file and a toml file together 
"""