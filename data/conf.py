import os

ABS_PATH = os.path.abspath(__file__) 
BASE_DIR = os.path.dirname(ABS_PATH) 
DATA_DIR = os.path.join(BASE_DIR) 
INPUTS = os.path.join(DATA_DIR, "inputs")
print(INPUTS) 
OUTPUTS = os.path.join(DATA_DIR, 'outputs') 