import os

from ..fileOperations import *
from ..stringOperations import *

def get_values_dict(ribName, newRibPackage, sharedPath):
  values_dict = {
              'Rib': ribName,
            'new_rib_package': newRibPackage,
            'shared_path': sharedPath,
    }
  return values_dict


def create_state_file(folderPath, newRibPackage, ribName):
  new_folder_for_state = folderPath + "/" + newRibPackage + "/state"
  may_be_create_folder(folderPath, new_folder_for_state)
  
  template_file_name = "RibState.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file,  template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "State.kt", new_folder_for_state)
  
  
  
def create_reducer_file(folderPath, newRibPackage, ribName):
  new_folder_for_state = folderPath + "/" + newRibPackage + "/state"
  may_be_create_folder(folderPath, new_folder_for_state)
  
  template_file_name = "RibReducer.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file,  template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "Reducer.kt", new_folder_for_state)


base_dir = os.path.dirname(os.path.abspath(__file__))
shared_template_files_path = "templates/shared"

def create_state_and_reducer_files(folderPath, newRibPackage, ribName):
  create_state_file(folderPath, newRibPackage, ribName)
  create_reducer_file(folderPath, newRibPackage, ribName)
