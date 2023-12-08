import os

from aocd import get_data
from cookiecutter.main import cookiecutter

day = input('Which day? ')
year = input('Which year? ')

try:
    input_data = get_data(day=int(day), year=int(year))
    folder_name = 'day_' + str(day)
    file_name = 'input.txt'

    directory = os.path.join(str(year), folder_name)
    file_path = os.path.join(directory, file_name)

    if not os.path.exists(directory):
        # Create project from the cookiecutter-pypackage/ template
        cookiecutter('folder-template',
             extra_context={'folder_name': folder_name})
        os.rename(folder_name, directory)

    with open(file_path, 'w+') as f:
        f.write(input_data)

except Exception as e:
    print(e)
