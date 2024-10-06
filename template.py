import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

logging.info('welcome everyone!')

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'app.py',
    'test.py'
]

for filepath in list_of_files:
    filepath = Path(filepath) #take care the forward & backward slash w.r.t machine config.
    filedir, filename=os.path.split(filepath)
    # print(filename)

    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info (f'creating directory {filedir} for {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'creating empty file : {filepath}')
    else:
        logging.info(f'{filename} is already exists')


