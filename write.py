import configparser
from src.python.img2text import exportData; 

config = configparser.ConfigParser()
config.read('.properties')
client=config.get('CSV','CLIENT')
menu_type=config.get('CSV','TYPE')

exportData(client,menu_type)