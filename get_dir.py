import os

def create_dir():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_path)

def remove_dir():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(new_path)
