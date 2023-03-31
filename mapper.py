def map_dict_to_string(map: dict[str, str]):
    envs = ""
    for k, v in map.items():
        envs = f"{envs}\n      - {k}={v}"
    return envs