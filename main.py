import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
     cam = cv2.VideoCapture(0)
     number = random.randint(1,100)
     img_name = "img"+str(number)+".png"
     result = True
     while(result):
          ret,frame = cam.read()
          print(ret)
          cv2.imwrite(img_name,frame)
          start_time = time.time
          result = False
     return img_name
     print("Snapshot Taken")
     cam.release()
     cv2.destroyAllWindows() 


def upload_file(img_name):
        """upload a file to Dropbox using API v2
        """
        access_token = 'vRgQrWVEVscAAAAAAAAAAfUFpKy91wr3SWbubpg-4QbGPDiwqW2jJ7Zo8SZctUbm'
        file_from = img_name
        file_to = '/Python/test.txt'+img_name
        dbx = dropbox.Dropbox(access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
     while(True):
          if((time.time()-start_time)>= 5):
               name = take_snapshot()
               upload_file(name)

main()


