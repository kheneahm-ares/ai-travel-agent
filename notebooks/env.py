import pathlib
from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent
ENV_FILE= BASE_DIR / ".env" #not interpolating 


def get_config():
    if ENV_FILE.exists():
        return Config(RepositoryEnv(ENV_FILE))
    from decouple import config as _decouple_config
    return _decouple_config #even if we don't have a file but have environment variables

config = get_config()