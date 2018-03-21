
from setuptools import setup, find_packages


def get_data_files():
    from os import listdir
    from os.path import join, isdir, isfile
    data = []
    root = "kernelspecs"
    dest_dir = join("share", "jupyter", "kernels")
    for folder in listdir(root):
        folder_path = join(root, folder)
        if not isdir(folder_path):
            continue
        target_dir = join(dest_dir, folder)
        files = []
        for file in listdir(folder_path):
            file_path = join(folder_path, file)
            if isfile(file_path):
                files.append(file_path)
        data.append((target_dir, files))
    return data


setup(
    name             = 'jupyter-cas-kernels',
    version          = '0.2.0',
    description      = 'Some kernels for Jupyter',
    install_requires = [ 'ipykernel' ],
    packages         = find_packages(exclude=['contrib', 'docs', 'tests']),  #
    data_files       = get_data_files()
)
