import os
import sys

def get_db_path(): 
    if getattr(sys, 'frozen', False): 
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0])) 
    else: 
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
    return os.path.join(base_dir, "haushalt.db")