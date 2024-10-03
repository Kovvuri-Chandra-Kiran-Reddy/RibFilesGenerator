import os

from ..fileOperations import *
from ..stringOperations import *

def get_values_dict(platformPath, ribName, newRibPackage, sharedPath):
  values_dict = {
              'Rib': ribName,
            'new_rib_package': newRibPackage,
            'shared_path': sharedPath,
            'platform_path': platformPath,
            'first_letter_small_rib_name': decapitalize_first_letter(ribName)
    }
  return values_dict
  
def common(platformFolderPath, newRibPackage, ribName, sharedFolderPath, fileSuffix):
  new_folder = platformFolderPath + "/" + newRibPackage
  
  template_file_name = "Rib" + fileSuffix
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), platform_template_files_path)
    
  content = read_content_from_file(final_path_for_template_file,  template_file_name)
    
  if(content == None):
    print("Failed to read content from template")
    exit(0)
    
  aaaaa_shared = transform_string(sharedFolderPath)
  aaaaa_platform = platform_transform_string(platformFolderPath)
    
  values_dict = get_values_dict(aaaaa_platform, ribName, newRibPackage, aaaaa_shared)
    
  updated_content = replace_content_with_dict_key_values(content, values_dict)
    
  write_content_to_new_file(updated_content, ribName + fileSuffix, new_folder)



def create_alias_file(platformFolderPath, newRibPackage, ribName, sharedFolderPath):
  common(platformFolderPath, newRibPackage, ribName, sharedFolderPath, "Alias.kt")


def create_interactor_file(platformFolderPath, newRibPackage, ribName, sharedFolderPath):
  common(platformFolderPath, newRibPackage, ribName, sharedFolderPath, "Interactor.kt")


def create_router_file(platformFolderPath, newRibPackage, ribName, sharedFolderPath):
  common(platformFolderPath, newRibPackage, ribName, sharedFolderPath, "Router.kt")


def create_view_file(platformFolderPath, newRibPackage, ribName, sharedFolderPath):
  common(platformFolderPath, newRibPackage, ribName, sharedFolderPath, "View.kt")


def create_interactorMP_factory_file(platformFolderPath, newRibPackage, ribName, sharedFolderPath):
  common(platformFolderPath, newRibPackage, ribName, sharedFolderPath, "InteractorMPFactory.kt")
  

def create_builder_file(platformFolderPath, newRibPackage, ribName, sharedFolderPath):
  common(platformFolderPath, newRibPackage, ribName, sharedFolderPath, "Builder.kt")


def create_xml_file(platformFolderPath, newRibPackage, ribName, sharedFolderPath):
  folder_path_for_xml_file_to_create = get_xml_file_folder_path(platformFolderPath) + "res/layout/"
  view_path = platform_transform_string(platformFolderPath)
  
  template_file_name = "rib_Rib.xml"
  final_path_for_template_file = os.path.join(os.path.dirname(os.path.dirname(base_dir)), platform_template_files_path)
  
  content = read_content_from_file(final_path_for_template_file,  template_file_name)
  
  if(content == None):
    print("Failed to read content from template")
    exit(0)
  
  aaaaa_shared = transform_string(sharedFolderPath)
  aaaaa_platform = platform_transform_string(platformFolderPath)
  
  values_dict = get_values_dict(aaaaa_platform, ribName, newRibPackage, aaaaa_shared)
  
  updated_content = replace_content_with_dict_key_values(content, values_dict)
  
  first_letter_small_rib_name = decapitalize_first_letter(ribName)
  
  write_content_to_new_file(updated_content, "rib_" + first_letter_small_rib_name + ".xml", folder_path_for_xml_file_to_create)

base_dir = os.path.dirname(os.path.abspath(__file__))
platform_template_files_path = "templates/platform"


def create_platform_rib_files(RIB_PLATFORM_PATH, RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME):
  create_alias_file(RIB_PLATFORM_PATH, NEW_RIB_PACKAGE, RIB_NAME, RIB_SHARED_PATH)
  create_interactor_file(RIB_PLATFORM_PATH, NEW_RIB_PACKAGE, RIB_NAME, RIB_SHARED_PATH)
  create_router_file(RIB_PLATFORM_PATH, NEW_RIB_PACKAGE, RIB_NAME, RIB_SHARED_PATH)
  create_view_file(RIB_PLATFORM_PATH, NEW_RIB_PACKAGE, RIB_NAME, RIB_SHARED_PATH)
  create_interactorMP_factory_file(RIB_PLATFORM_PATH, NEW_RIB_PACKAGE, RIB_NAME, RIB_SHARED_PATH)
  create_builder_file(RIB_PLATFORM_PATH, NEW_RIB_PACKAGE, RIB_NAME, RIB_SHARED_PATH)
  create_xml_file(RIB_PLATFORM_PATH,NEW_RIB_PACKAGE, RIB_NAME, RIB_SHARED_PATH)
