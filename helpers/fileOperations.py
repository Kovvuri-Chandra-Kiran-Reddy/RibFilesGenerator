import os

# create folder if its not exist
def may_be_create_folder(folderPath, newFolderName):
  full_path = os.path.join(folderPath, newFolderName)
  if not os.path.exists(full_path):
    os.makedirs(full_path)

# read content from given file.
def read_content_from_file(folderPath, fileName):

  file_path = os.path.join(folderPath, fileName)

  if not os.path.exists(file_path):
    return None

  with open(file_path, 'r') as file:
    content = file.read()

  return content
  
  
# write content to the file
def write_content_to_new_file(content, fileName, folderPath):
  if not os.path.exists(folderPath):
    os.makedirs(folderPath)

  new_file_path = os.path.join(folderPath, fileName)

  with open(new_file_path, 'w') as new_file:
    new_file.write(content)
