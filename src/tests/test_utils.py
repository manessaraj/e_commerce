import inspect
import random
import string
from typing import Any, Type, get_args, get_origin

from pydantic import BaseModel


def random_string(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def random_value_for_type(field_type: Type[Any]) -> Any:
    """
    Generates a random value based on the provided type.
    """
    origin_type = get_origin(field_type) or field_type

    if inspect.isclass(origin_type) and issubclass(origin_type, BaseModel):
        return create_random_object(
            origin_type
        )  # Recursively create an instance of the model

    if origin_type == list:
        element_type = get_args(field_type)[0]
        return [
            random_value_for_type(element_type) for _ in range(random.randint(1, 5))
        ]

    if origin_type == int:
        return random.randint(1, 100)
    elif origin_type == float:
        return random.random() * 100
    elif origin_type == str:
        return random_string()
    elif origin_type == bool:
        return random.choice([True, False])

    else:
        raise ValueError(f"No random generator implemented for type {origin_type}")


def create_random_object(model: Type[BaseModel], exclude: set = None) -> BaseModel:
    """
    Creates an instance of the given Pydantic model class with random values,
    excluding specified fields.
    """
    exclude = exclude or set()
    values = {}
    for field_name, field_type in model.__annotations__.items():
        if field_name not in exclude:
            values[field_name] = random_value_for_type(field_type)
    return model(**values)
