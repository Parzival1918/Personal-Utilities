import os

def get_dir_size(path: str = './'): # Exclude files in subdirectories
    total_size = 0
    files = os.listdir(path)
    for f in files:
        fp = os.path.join(path, f)
        total_size += os.path.getsize(fp)

    # for dirpath, dirnames, filenames in os.walk(path):
    #     for f in filenames:
    #         fp = os.path.join(dirpath, f)
    #         total_size += os.path.getsize(fp)

    return total_size

def get_dir_files(path: str = './', include_dirs: bool = False): # Exclude files in 
                                                                 # subdirectories
    all_files = os.listdir(path)
    files = []
    dirs = []
    for f in all_files:
        fp = os.path.join(path, f)
        if os.path.isfile(fp):
            files.append(f)
        if include_dirs and os.path.isdir(fp):
            dirs.append(f)

    # for dirpath, dirnames, filenames in os.walk(path):
    #     for f in filenames:
    #         # fp = os.path.join(dirpath, f)
    #         files.append(f)

    return files, dirs

def get_file_size(path: str):
    return os.path.getsize(path)

# Function to return the size of a file in kB, MB, GB, etc.
def transform_file_size(size: int) -> str:
    if size < 1024:
        return "B"
    elif size < 1024**2:
        return "kB"
    elif size < 1024**3:
        return "MB"
    elif size < 1024**4:
        return "GB"
    elif size < 1024**5:
        return "TB"
    else:
        return "PB"
    
# Function to get the different file types in a directory and 
# the number of files of each type
def get_file_types(files: list[str], ignore_hidden: bool = True) -> dict:
    file_types = {}
    file_types['none'] = 0
    for f in files:
        if f[0] == '.' and ignore_hidden:
            continue
        elif f[0] == '.' and not ignore_hidden:
            # count how many '.' are in the filename
            # if more than 1, it's a hidden file
            if f.count('.') == 1:
                file_types['none'] = 1
                continue
        
        f_type = f.split('.')[-1]
        if f_type in file_types:
            file_types[f_type] += 1
        else:
            file_types[f_type] = 1
    return file_types