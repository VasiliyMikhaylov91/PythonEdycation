import os

root_path = '.venv'

with open('.gitignore', 'w', encoding='utf8') as fl:
    for root, dirs, files in os.walk(root_path):
        for name in files:
            fl.write(os.path.join(root, name)+'\n')