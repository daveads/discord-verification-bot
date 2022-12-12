from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


import logging
from rich.logging import RichHandler

logging.basicConfig(format='%(levelname)s ::: %(message)s')


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

    def channel_id(self, chn):

        if chn in self.data['channels_id']:
            return self.data['channels_id'][chn]

 

    def gender(self, gender):
        if gender in self.data["gender"]:
            return self.data['gender'][gender]


    def age_roles(self, age):
        if age in self.data['age_role']:
            return self.data['age_role'][age]


    def verfy_roles(self, role):
        if role in self.data['roles']:
            return self.data['roles'][role]

    

    """
    def roles(self, role):

        #verf_roles
        if role == "self_ver":
            self_ver = self.data['verf_roles']['self_ver']
            return self_ver

        if role == "age_ver":
            self_ver = self.data['verf_roles']['age_ver']
            return self_ver



        # gender roles 
        if role == "male" :
            return self.data['gender']['male'] 

        if role == "female" :
            return self.data['gender']['female']
        
        if role == "trans_female" :
            return self.data['gender']['trans_female']
        
        if role == "non_binary":
            return self.data['gender']['non_binary']
        
        if role == "agender":
            return self.data['gender']['agender']
        
        if role == "bigender":
            return self.data['gender']['bigender']
        
        if role == "genderfluid": 
            return self.data['gender']['genderfluid']


        #age roles
        if role == '18-22':
            return self.data['age_role']['18-22']

        if role == '23-27':
            return self.data['age_role']['23-27']

        if role == '28-30+':
            return self.data['age_role']['28-30+']
    """




"""
see if it is possible to write directly into the .toml file
it should be possible tho

rather than using a txt file and a toml file together 
"""