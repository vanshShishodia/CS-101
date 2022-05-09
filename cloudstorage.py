import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token="sl.BHSpW38JfRFdfKY20a3J97ImlREVV2vnjugz6IZw-QknFGYyvU3YGBJ0iV7QfYekr7wnkfOrnyR4P4qSUzXYN5Q5-SOPxCc922RLvOIRZ8JyigbzDcNgn0k90PQ8084WSHU7qqD076Y"
    transferData=TransferData(access_token)
    file_from=str(input("Please enter the folder path to transfer:"))
    file_to=input("enter the full path to upload on dropbox:")
    transferData.upload_file(file_from,file_to)
    print("Files have been transfered.")

main()