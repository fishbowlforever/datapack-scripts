# a simple script that upgrades pre minecraft 1.21.2/3 recipes to 1.21.2/3 recipes
# author: fishbowlforever

import json
import os
from glob import iglob

oldPath = "datapackName/data/datapack_namespace/recipe(s)/" # replace with your pre 1.21.2 path
newPath = "datapackName/data/datapack_namespace/recipe/" # replace with your 1.21.2+ 

if not oldPath.endswith("/"): oldPath += "/"
if not newPath.endswith("/"): newPath += "/"

def upgrade(data):
    match type(data).__name__:
        case "list":
            newdata = []
            for datum in data:
                datum = upgrade(datum)
                newdata.append(datum)
            data = newdata
        case "dict":
            for key in data.keys():
                if key == "item":
                    return data[key]
                elif key == "tag":
                    return "#" + data[key]
                else:
                    data[key] = upgrade(data[key])
        case "str":
            pass
        case "int":
            pass
        case _:
            print("unexpected other type: " + type(data).__name__)
    return data

for sourcePath in iglob(oldPath+"**/*.json",recursive = True):
    sourcePath = sourcePath.replace(os.sep, '/')
    data = None # how can i init a var?
    with open(sourcePath, "r") as f:
        data = json.loads(f.read())
        data = upgrade(data)
    
    targetPath = sourcePath.replace(oldPath, newPath)
    os.makedirs(os.path.dirname(targetPath), exist_ok = True)
    with open(targetPath, "w") as f:
        f.write(json.dumps(data, indent = 4))