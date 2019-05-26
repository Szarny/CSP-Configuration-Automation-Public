from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from IO import out


def is_validate_url(url: str) -> bool:
    """
    Perform URL validation check by `django.core.validators.URLValidator`.   
    """

    validator: URLValidator = URLValidator()

    try:
        validator(url)
        return True
    except ValidationError as err:
        out.error(err)
        return False