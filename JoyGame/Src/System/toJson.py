import json


def config_wt(file_name, config, display="False"):
    with open(str(file_name) + ".json", "w") as f:
        json.dump(config, f, sort_keys=True, indent=4, separators=(',', ': '))
        if not display:
            print("Save %s completion" % file_name.split("/")[-1])


def config_rd(file_name, display="False"):
    with open(str(file_name) + ".json", 'r') as load_f:
        if not display:
            print("Load %s completion" % file_name.split("/")[-1])
        return json.load(load_f)
