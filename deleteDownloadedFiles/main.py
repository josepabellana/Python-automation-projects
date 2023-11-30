import os

file_path = '/Users/josep/Downloads/BoardingPass.pdf'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print('File has been successfully been deleted')
else:
    print('File does not exist!')