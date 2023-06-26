import os


class removefiles():
    
    
    def remove(self):
        
        folder_path = os.getcwd()
        file_list = os.listdir(folder_path)

        for file_name in file_list:
            if file_name.endswith(".mp3"):
                file_path = os.path.join(folder_path, file_name)  
                if os.path.isfile(file_path):  
                    os.remove(file_path)  

r = removefiles()