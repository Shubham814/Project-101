# Importing modules 
import dropbox
import os

class UploadFiles(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)

        for root,files in os.walk(fileFrom):

            for filename in files:

                # construct the full local path
                local_path = os.path.join(root, filename)


                # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), fileTo)

        print("___________________________")
        print("    !!Congratulations!!    ")
        print("Files Uploaded Successfully")
        print("___________________________")


def main():
    # Getting the Access Token and storing it into a Variable
    token = open('access_token.txt','r')
    access_token = token.read()

    db = UploadFiles(access_token)

    print(" ________________________________")
    print("|--------------------------------|")
    print("|--UPLOAD YOUR FILES TO DROPBOX--|")
    print("|--------------------------------|")
    print("|________________________________|")

    print("\n\n") # For Spaces

    fileFrom = input("Enter the File Path you want to Upload: ")
    fileTo = input("Enter the Dropbox path Where you want to Upload: ")

    db.upload_files(fileFrom,fileTo)


# Calling the Function
main()