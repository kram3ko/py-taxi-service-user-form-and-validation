from django.core.validators import BaseValidator
from django.utils.translation import gettext_lazy as _


class ExactLenValidator(BaseValidator):
    message = _("Ensure this value has exactly %(limit_value)s "
                "characters (it has %(show_value)s).")
    code = "exact_length"

    def compare(self, input_length, required_length):
        return input_length != required_length

    def clean(self, value):
        return len(value)

    def __call__(self, value):
        self.show_value = len(value)
        super().__call__(value)


class FirstUpperLetter(BaseValidator):
    message = _("Ensure the first three characters are uppercase letters.")
    code = "three_upper"

    def compare(self, value, required_count):
        first_part = value[:required_count]
        return not (first_part.isupper() and first_part.isalpha())

    def clean(self, value):
        return value


class LastDigits(BaseValidator):
    message = _("Ensure the last five characters are digits.")
    code = "last_digits"

    def compare(self, value, required_count):
        return not (value[-required_count:].isdigit())

    def clean(self, value):
        return value
