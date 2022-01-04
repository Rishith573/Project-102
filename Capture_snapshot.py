import cv2
import dropbox
import random
import time

start_time = time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result=True

    while (result):
        ret, frame = videoCaptureObject.read()
        img_name = 'img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result=False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'sl.A_Sqadirt9P_E8m3lhgMdvyYq021zGKDi2cKJsUuGCOY8J77grmsx2H2zvvwsgWxlWwFsinR1rVbIJM3ThSJ67pABG-vtjgYaIVDQ1KKAmul8o9Rzaqr1r76rnyq-6QFCK_obJWNdTcS'
    file=img_name
    file_from=file
    file_to='/testFolder'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")
def main():
    while (True):
        if (time.time()-start_time)>=5:
            name=take_snapshot()
            upload_file(name)
main()
