from PIL import Image
from pillow_heif import register_heif_opener
import os,sys
register_heif_opener()
try:
    source = sys.argv[1]
except:
    source = os.getcwd()
try:
    dest = sys.argv[2]
except:
    dest = os.path.join(source,"result")
files = os.listdir(source)
heic_files = [i for i in files if 'HEIC' in i]
os.makedirs(dest,exist_ok=True)
for i in heic_files:
    try:
        TargetFile= f'{dest}/{i}'.replace("HEIC",'jpg')
        tfile = open (TargetFile,'wb')
        image = Image.open(os.path.join(source,i))
        image.save(tfile)
        image.close()
    except Exception as e:
        print("error with ",e)

