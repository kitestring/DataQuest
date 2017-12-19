import os
import pprint

from jsonAPI import JSON_Tools


JSON_Tools = JSON_Tools()
FileName = os.path.join(os.getcwd(),'NFL_stats.json')
dataset = JSON_Tools.Load_Data(FileName)



pp = pprint.PrettyPrinter(indent=4,width=80,depth=20)
pp.pprint(dataset)

