import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "image"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        start_time = time.time
        result = False
    return(imageName)
    print("Snapshot Taken!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = 'sl.BJn4KnKazHQPnUsfJNjoUtZE1KddZc4oKGFO88tNNJI9JzGydUOqKfUxZuiKHenz3m9duSlrrhab5j0XU0Fx_NtEsETYdzdQcWGscIVceYBhAPPqutL-9gP_t9GRLW3QmFArJTY'
    file = imageName
    file_from = file
    file_to = '/newFolder1/'+(imageName) 
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode = dropbox.files.WriteMode.overWrite)
        print("Files Uploaded")
            
def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_file(name)

main()
