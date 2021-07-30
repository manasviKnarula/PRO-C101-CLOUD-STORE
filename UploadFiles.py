import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path=os.path.join(root,file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))








def main():
    access_token = "FQfkxi2R0WkAAAAAAAAAAR3MNfYP_0YFMEzQ4rU3xp8OtGPxW2RzwxaS_Q5nSzHW"
    transferData = TransferData(access_token)

    file_from = input("Please enter the file path: ")
    file_to = input("Please enter the full path")
    transferData.upload_files(file_from, file_to)
    print("YAY! Your file has been moved 🥳🥳🥳")







main()
