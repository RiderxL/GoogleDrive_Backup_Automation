from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

prompts = [
        'up : Upload',
        'dl : Download',
        'cr : Create',
        'ls : List_Files\n'
]

class Drive:
    def upload(self, file_path):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        
        drive = GoogleDrive(gauth)
        f = drive.CreateFile()
        f.SetContentFile(file_path)
        f.Upload()

    def download(self):
        print("Download File")
    
    def create(self):
        print("Create File")
        
    def list_file(self):
        print("List File")

class Main(Drive):
    def __init__(self, command, file_path):
        self.command = command
        self.file_path = file_path
        
    def process_choice(self, choice):
        functions = {'up' : self.upload(self.file_path),
                    'dl' : self.download,
                    'cr' : self.create,
                    'ls' : self.list_file}
                
        func = functions[choice]
    
        if callable(func):
            func()
        
        else:
            print("Not found in the index")

if __name__ == "__main__":
    
    for prompt in prompts:
        print(prompt)
    
    curr_input = input("Input choice and file: ")
    
    command, file_path = map(str, curr_input.split())
    main = Main(command, file_path)
    
    main.process_choice(command)