from os import sep
from glob import iglob

recipePath = "DatapackName/data/datapack_namespace/recipe(s)/" #replace with your path
functionPath = "DatapackName/data/datapack_namespace/function(s)/" #replace with your path
namespace = "datapack_namespace" #replace with your namespace

if not functionPath.endswith("/"): functionPath = functionPath + "/"
if not recipePath.endswith("/"): recipePath = recipePath + "/"

# os.makedirs(functionPath, exist_ok=True) #uncomment to create function folder if it doesn't exist yet

with open(functionPath + "unlock_all_recipes.mcfunction","w+") as f:
    for abspath in iglob(recipePath+"**/*.json",recursive = True):
        abspath = abspath.replace(sep, '/') # normalize path for minecraft
        relpath = abspath.replace(recipePath, "") #relative path in recipe folder
        namepart = relpath.rsplit( ".", 1 )[0] # name of path without extension
        f.write(f"recipe give @s {namespace}:{namepart}\n")