
def replace_content_with_dict_key_values(content, values_dict):
  for key, value in values_dict.items():
    content = content.replace(f'{{{key}}}', value)
  return content
  
# tranfrom string to get required package for shared
def transform_string(input_string):
  start_index = input_string.find('in/porter')
  if start_index != -1:
    relevant_part = input_string[start_index:]
  else:
    print("The string does not contain 'in/'")
    return None
    
  transformed_string = relevant_part.replace('/', '.')
    
  transformed_string = transformed_string.replace('in.porter', '`in`.porter')
    
  return transformed_string

# tranfrom string to get required package for platform
def platform_transform_string(input_string):
  start_index = input_string.find('com/theporter')
  if start_index != -1:
    relevant_part = input_string[start_index:]
  else:
    print("The string does not contain 'com/theporter'")
    return None
  
  transformed_string = relevant_part.replace('/', '.')

  return transformed_string

# get folder path to create new xml file
def get_xml_file_folder_path(input_string):
  start_index = input_string.find('java/com')
  if start_index != -1:
    relevant_part = input_string[:start_index]
  else:
    print("The string does not contain 'com/theporter'")
    return None
  
  transformed_string = relevant_part.replace('/', '.')

  return relevant_part
  
# make the first character of the string to lower case
def decapitalize_first_letter(input_string, upper_rest=False):
    return ''.join([input_string[:1].lower(), (input_string[1:].upper() if upper_rest else input_string[1:])])
