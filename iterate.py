from msilib.schema import Directory
import os


folder_to_parse=[]
nudos_to_parse=[]

def search(path):
    fpath=path

    with os.scandir(fpath) as Directory:

        for entry in Directory:
            path2=entry.path
            
            if entry.is_file()==False:

                print("\n",entry.name,"\n")

                search(path2)

                if (fpath in nudos_to_parse)==False:
                    nudos_to_parse.append(entry.name)

            else:
                print(entry.name)

                if (fpath in folder_to_parse)==False:    
                    folder_to_parse.append(fpath) #verify path not repeated
                

        #for entry in it:
         #   if entry.name.endswith(".pdf") and entry.is_file():
          #      print(entry.name, entry.path)
    
def filesearch(path):
    search(path)
    return folder_to_parse
filesearch(fr"path")
print(folder_to_parse)
print(nudos_to_parse)
