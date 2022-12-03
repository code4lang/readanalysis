import re, os, subprocess
from subprocess import PIPE

def convert_toimage(path):
    print("convert_toimage")

    #path=path+".pdf"

    position=path[::-1].find("\\")
    doc=path[len(path)-position:]
    path_of_the_directory=path[:len(path)-position]
    
    output=doc.replace("png","tiff")
    
    cmd = ["magick","-density","500 ",doc,"-alpha", "off", output]
    result=subprocess.Popen(
            cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=path_of_the_directory
        )
    output, error = result.communicate()
    #print(output,"\n", error) ""
    
def extract_totext(path):
    print("extract_totext")

    command="tesseract "+path+".tiff "+path
    subprocess.run(command)


def get_text(path):
    print("get_text")
   
    command="pdftotext -enc UTF-8 "+'"'+path+'" '+'"'+path+".txt"+'" '    #+".pdf"
    subprocess.run(command)

def clean(path):
    print("clean")
    
    args = ("del", "-rf", path+"*.txt")
    subprocess.call('%s %s %s' % args, shell=True)
def delspace(path):
    return


def extract(path):
    #clean from special cacharacters, avoid injections
    print(path)
    path=fr"{path}"
    get_text(path)
    
    minsize=5
    with open(path+".txt","r", encoding='utf8') as f:
        filesize=len(f.readline())
        if filesize>minsize:
            content= f.read()
   
    if  filesize<minsize:
        convert_toimage(path)
        extract_totext(path)
        with open(path+".txt","r") as f:
            content= f.read()
    #clean(path)
    print("done")
    print(content)
    return content


#extract("03_03955321_correcto")
def extract_in_folder(path):
    path=fr"{path}"
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():                #entry.name.endswith(".pdf") and 
                print(entry.name, entry.path)
                
                #file=entry.path.strip("pdf").strip(".")
                file=entry.path
                print(file)
                extract(file)
extract_in_folder(fr"C:\Users\bdefe\Desktop\pdf_to_excelanalysis\data\images")
