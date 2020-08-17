import pathlib
import json

class SecretsLoader():
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def load_secrets(self, path):
        """
        @param path:: Path to the secrets file (always absolute path)
        """
        path = pathlib.Path(path)
        print(path)
        if path.is_absolute() and path.exists():
            with path.open('r') as f:
                data = json.load(f)
                print(data)
