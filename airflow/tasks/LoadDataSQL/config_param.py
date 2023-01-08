import pathlib
from dotenv import dotenv_values

def config_param(filename: str, section: str):

    script_path = pathlib.Path(__file__).parent.parent.resolve()
    config_file = dotenv_values(f"{script_path}/{filename}")
    config = config_file[f"{section}"]

    return config
