import os
from utils import assert_dir
from utils import assert_file
from utils import is_file_or_dir


class ResourceValidator:


    def __init__(self):
        pass


    def assert_resources(self, files, directories, either ):
        
        for file in files:
            assert_file(os.path.abspath(file))

        for dir in directories:
            assert_dir(os.path.abspath(dir))

        for f in either:
            if not is_file_or_dir(os.path.abspath(f)):
                print(f'{f} is nor file nor direcotriy')
                exit(1)
        
        
