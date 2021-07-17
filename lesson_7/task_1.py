import os


ROOT = os.path.dirname(__file__)
folder = 'my_project'
sub_folders = {'settings', 'mainapp', 'adminapp', 'authapp'}

folder_path = os.path.join(ROOT, folder)

if not os.path.exists(folder_path):
    os.mkdir(folder_path)

for sub_folder in sub_folders:
    sub_folder_path = os.path.join(folder_path, sub_folder)
    if not os.path.exists(sub_folder_path):
        os.mkdir(sub_folder_path)

