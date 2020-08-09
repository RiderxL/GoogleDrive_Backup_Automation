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
       folder_id = os.getenv('GOOGLE_DRIVE_FOLDER_ID')
       filename_with_ext = os.path.basename(file_path)
       filename, file_ext = os.path.splitext(filename_with_ext)
        
    def download(self):
        print("Download File")
    
    def create(self):
        print("Create File")
        
    def list_file(self):
        print("List File")

class Main(Drive):
    def __init__(self, command, usr_input, file_path):
        self.command = command
        self.usr_input = usr_input
        
    def process_choice(self, choice):
        functions = {'up' : self.upload(file_path),
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
    
    command, usr_input, file_path = curr_input.split()
    main = Main(command, usr_input)
    
    main.process_choice(command)