import json


def config_wt(file_name, config):
    with open(str(file_name) + ".json", "w") as f:
        json.dump(config, f, sort_keys=True, indent=4, separators=(',', ': '))
        print("Save %s completion" % file_name)


def config_rd(file_name):
    with open(str(file_name) + ".json", 'r') as load_f:
        print("Load %s completion" % file_name)
        return json.load(load_f)
