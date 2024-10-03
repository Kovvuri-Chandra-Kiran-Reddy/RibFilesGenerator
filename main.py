import os

from helpers.sharedHelpers.shared_rib_files_creator import *
from helpers.platformHelpers.platform_rib_files_creator import *

if __name__ == "__main__":

  NEW_RIB_PACKAGE = input("enter the package name under which new folder u wanted to create new rib: ").strip() # should contain all small characters.
  
  print("\nNOTE: the rib name you enter will be prefix to all files like <RIB_NAME>.interactor, make sure u enter rib name in UpperCamelCase")
  RIB_NAME = input("enter rib name: ").strip() # should provide like u giving for classes: like first letter also capital.
  
  print("\nNOTE: Kindly exclude new package which we gonna create for new rib for entering platform rib path below")
  
  RIB_PLATFORM_PATH = input("Please enter platform rib path where u wanted to create platform rib files: ").strip()
  
  if(len(RIB_PLATFORM_PATH) == 0 or "theporter/android/customerapp" not in RIB_PLATFORM_PATH):
    print("\nPlese enter correct platform rib path where u wanted to create platform rib files!!!")
    exit(0)
  
  print("\nNOTE: Kindly exclude new package which we gonna create for new rib for entering shared rib path below")
  
  RIB_SHARED_PATH = input("Please enter shared rib path where u wanted to create rib files (u need to exclude new package which we gonna create): ").strip()
    
  if(len(RIB_SHARED_PATH) == 0 or "in/porter/customerapp/shared" not in RIB_SHARED_PATH):
    print("\nPlese enter correct shared rib path where u wanted to create platform rib files!!!")
    exit(0)

  create_shared_rib_files(RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME)
  create_platform_rib_files(RIB_PLATFORM_PATH, RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME)

  print("\nHurray!, all required files were created successfully!! 🚀🚀 please change ProductFlow in EventIdentifiers file.")

