#change all extension of the files in folder

import os

path_folder = input('Enter the path of folder :').replace('"', '')

#create dictionary of change extension

old_new_extension_dict = {}
end_word = ''
while end_word != 'stop':
    old_extension = input('enter old extension: ')
    new_extension = input('enter new extension: ')
    old_new_extension_dict[old_extension] = new_extension
    end_word = input('enter word (next or stop) if you name all extension: ')
print(old_new_extension_dict)

#change extension every file in folder from dictionary

for file_name in os.listdir(path_folder):

    #find extension of the file
    base_file, extension = os.path.splitext(file_name)
    extension = extension.replace('.','')

    if extension in old_new_extension_dict:
        new_file_name = base_file + '.' + old_new_extension_dict[extension]

        #Create the old and new path every file
        old_path = os.path.join(path_folder, file_name)
        new_path = os.path.join(path_folder, new_file_name )

        #Rename the file
        os.rename(old_path, new_path)