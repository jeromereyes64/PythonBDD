from configparser import ConfigParser

#create object
config = ConfigParser()

config.read("config.cfg")

print(config.get("section","username"))