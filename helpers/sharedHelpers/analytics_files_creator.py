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

# analytics files creator
def create_analytics_file(folderPath, newRibPackage, ribName):
  # creating folder path for analytics files in shared
  new_folder_for_analytics = folderPath + "/" + newRibPackage + "/analytics"
  
  # this function will create folder if ints not exist
  may_be_create_folder(folderPath, new_folder_for_analytics)
  
  # this file has default code for analytics file.
  template_file_name = "RibAnalytics.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file,  template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
        
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "Analytics.kt", new_folder_for_analytics)
  

def create_event_identifers_file(folderPath, newRibPackage, ribName):
  new_folder_for_analytics = folderPath + "/" + newRibPackage + "/analytics"
  may_be_create_folder(folderPath, new_folder_for_analytics)
  
  template_file_name = "RibEventIdentifier.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file,  template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
        
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "EventIdentifier.kt", new_folder_for_analytics)


base_dir = os.path.dirname(os.path.abspath(__file__))
shared_template_files_path = "templates/shared"


def create_analytics_and_event_identifier_files(folderPath, newRibPackage, ribName):
  create_analytics_file(folderPath, newRibPackage, ribName)
  create_event_identifers_file(folderPath, newRibPackage, ribName)
