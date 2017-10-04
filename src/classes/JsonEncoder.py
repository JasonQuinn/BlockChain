import json

from src.classes.dto.Serializable import Serializable


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Serializable):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
