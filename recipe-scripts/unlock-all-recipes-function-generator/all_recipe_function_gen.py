from os import walk

recipePath = "DatapackName/data/datapack_namespace/recipe(s)" #replace with your path
functionPath = "DatapackName/data/datapack_namespace/function(s)" #replace with your path
namespace = "datapack_namespace" #replace with your namespace

# os.makedirs(functionPath, exist_ok=True) #uncomment to create function folder if it doesn't exist yet

with open(functionPath + "unlock_all_recipes.mcfunction","w+") as f:
    for (dirpath, dirnames, filenames) in walk(recipePath):
        suffix = dirpath.replace(recipePath, "")
        suffix = suffix.replace("\\","/") # windows paths are weird
        if suffix != "":
            suffix += "/"
        for filename in filenames:
            namepart = filename.rsplit( ".", 1 )[0]
            f.write("recipe give @s " + namespace + ":" + suffix + namepart + "\n")