import os
import json


def config_wt(file_name, config, display="False"):
    if os.path.exists(str(file_name) + ".json"):
        with open(str(file_name) + ".json", "w") as f:
            json.dump(config, f, sort_keys=True, indent=4, separators=(',', ': '))
            if display:
                print("Save %s completion" % file_name.split("/")[-1])
    else:
        print("%s\nis not exists" % file_name)


def config_rd(file_name, display="False"):
    if os.path.exists(str(file_name) + ".json"):
        with open(str(file_name) + ".json", 'r') as load_f:
            if display:
                print("Load %s completion" % file_name.split("/")[-1])
            return json.load(load_f)
    else:
        print("%s\nis not exists" % file_name)
