import json
from tool_flask.common.constant import SHOP_LIST_JSON

class BizParams:
    DEFAULT_VALUES = SHOP_LIST_JSON

    def __init__(self, data=None):
        if data is None:
            data = {}
        for key, default_value in SHOP_LIST_JSON.items():
            setattr(self, key, data.get(key, default_value))

    def to_json(self):
        body = json.dumps(self.__dict__, ensure_ascii=False, indent=4)
        return json.loads(body)

    def update_params(self, **kwargs):
        for param, value in kwargs.items():
            if param in SHOP_LIST_JSON:
                setattr(self, param, value)
            else:
                print(f"Parameter {param} does not exist.")

# Example usage
json_data = SHOP_LIST_JSON
params = BizParams(json_data)

