import os
import shutil

template_path = 'templates'
ROOT = os.path.join(os.path.dirname(__file__), 'my_project')
path_to_templates = os.path.join(ROOT, template_path)

if not os.path.exists(path_to_templates):
    os.mkdir(path_to_templates)

for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith('.html'):
            path = root.split('/')
            if path[len(path) - 2] != template_path:
                continue
            new_template_sub_folder = os.path.join(path_to_templates, path[len(path) - 1])
            if not os.path.exists(new_template_sub_folder):
                os.mkdir(new_template_sub_folder)
            file_destination_copy_path = os.path.join(new_template_sub_folder, file)
            if not os.path.exists(file_destination_copy_path):
                shutil.copyfile(os.path.join(root, file), file_destination_copy_path)

