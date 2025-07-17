# data_loader_q19.py

import json

def load_config_q19(path_q19):
    with open(path_q19) as f_q19:    # no FileNotFoundError catch
        data_q19 = json.load(f_q19)

    # BUG: assumes keys exist
    return {
        "mode": data_q19["modo"],     # typo: should be "mode"
        "threshold": data_q19["threshold"]
    }