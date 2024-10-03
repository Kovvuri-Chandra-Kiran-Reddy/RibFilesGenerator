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
  
def create_params_file(folderPath, newRibPackage, ribName):
  new_folder = folderPath + "/" + newRibPackage
  
  template_file_name = "RibParams.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file, template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "Params.kt", new_folder)
  

def create_listener_file(folderPath, newRibPackage, ribName):
  new_folder = folderPath + "/" + newRibPackage
  
  template_file_name = "RibListener.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file, template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)

  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "Listener.kt", new_folder)
  
def create_router_file(folderPath, newRibPackage, ribName):
  new_folder = folderPath + "/" + newRibPackage
  
  template_file_name = "RibRouter.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file, template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "Router.kt", new_folder)

def create_interactor_file(folderPath, newRibPackage, ribName):
  new_folder = folderPath + "/" + newRibPackage
  
  template_file_name = "RibInteractor.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file, template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "Interactor.kt", new_folder)

def create_builder_file(folderPath, newRibPackage, ribName):
  new_folder = folderPath + "/" + newRibPackage
  
  template_file_name = "RibBuilder.kt"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), shared_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file, template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa = transform_string(folderPath)
  
  values_dict = get_values_dict(ribName, newRibPackage, aaaaa)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  write_content_to_new_file(updated_content, ribName + "Builder.kt", new_folder)


base_dir = os.path.dirname(os.path.abspath(__file__))
shared_template_files_path = "templates/shared"


def create_remaining_shared_rib_files(folderPath, newRibPackage, ribName):
  create_params_file(folderPath, newRibPackage, ribName)
  create_router_file(folderPath, newRibPackage, ribName)
  create_builder_file(folderPath, newRibPackage, ribName)
  create_listener_file(folderPath, newRibPackage, ribName)
  create_interactor_file(folderPath, newRibPackage, ribName)
