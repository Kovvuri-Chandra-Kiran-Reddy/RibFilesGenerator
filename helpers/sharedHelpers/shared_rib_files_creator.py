import os

from helpers.fileOperations import *
from helpers.stringOperations import *
from helpers.sharedHelpers.analytics_files_creator import *
from helpers.sharedHelpers.state_files_creator import *
from helpers.sharedHelpers.view_files_creator import *
from helpers.sharedHelpers.remaining_files_creator import *


# to get dic
def get_values_dict(ribName, newRibPackage, sharedPath):
  values_dict = {
              'Rib': ribName,
            'new_rib_package': newRibPackage,
            'shared_path': sharedPath,
    }
  return values_dict
  
  
def create_shared_rib_files(RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME):
  create_analytics_and_event_identifier_files(RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME)
  create_state_and_reducer_files(RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME)
  create_vm_presenter_and_vm_mapper_files(RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME)
  create_remaining_shared_rib_files(RIB_SHARED_PATH, NEW_RIB_PACKAGE, RIB_NAME)

