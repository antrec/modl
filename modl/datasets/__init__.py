import os
from .hcp import get_hcp_data

def get_data_dirs(data_dir=None):
    paths = []

    # Check data_dir which force storage in a specific location
    if data_dir is not None:
        paths.extend(data_dir.split(os.pathsep))

    # If data_dir has not been specified, then we crawl default locations
    if data_dir is None:
        global_data = os.getenv('SHARED_DATA')
        if global_data is not None:
            paths.extend(global_data.split(os.pathsep))

        local_data = os.getenv('DATA')
        if local_data is not None:
            paths.extend(local_data.split(os.pathsep))

        paths.append(os.path.expanduser('~/data'))
    return paths