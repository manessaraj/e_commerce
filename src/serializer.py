from pydantic import BaseModel

from src.models.models import Product, User


class Serailizer(object):
    def __init__(self, model: BaseModel, patch_model: BaseModel | None = None):
        self.model = model
        self.patch_model = patch_model

    def _validate_patch_model(self, obj):
        raise NotImplementedError

    def _serailize(self, obj):
        if self.patch_model:
            serailzed_obj = self.patch_model(**obj)
        patched = False
        for key, value in (serailzed_obj.model_dump() or {}).items():
            if value is None:
                patched = True
                break
        if not patched or not self.patch_model:
            serailzed_obj = self.model(**obj)

        return serailzed_obj

    def serialize(self, obj, many=False):
        if many:
            return [self._serailize(o) for o in obj]
        return self._serailize(obj)

    def deserialize(self, obj):
        return obj.model_dump()


product_serializer = Serailizer(Product)
user_serializer = Serailizer(User)
