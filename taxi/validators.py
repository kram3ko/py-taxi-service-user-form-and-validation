from django.core.validators import BaseValidator
from django.utils.translation import gettext_lazy as _


class ExactLenValidator(BaseValidator):
    message = _("Ensure this value has exactly %(limit_value)s "
                "characters (it has %(show_value)s).")
    code = "exact_length"

    def compare(self, a, b):
        return a != b

    def clean(self, x):
        return len(x)

    def __call__(self, value):
        self.show_value = len(value)
        super().__call__(value)


class FirstThreeUpperLetter(BaseValidator):
    message = _("Ensure the first three characters are uppercase letters.")
    code = "thee_upper"

    def __init__(self):
        super().__init__(limit_value=None)

    def compare(self, a, b):
        return not (a[:3].isupper() and a[:3].isalpha())

    def clean(self, x):
        return x


class LastFiveDigits(BaseValidator):
    message = _("Ensure the last five characters are digits.")
    code = "last_five_digits"

    def __init__(self):
        super().__init__(limit_value=None)

    def compare(self, a, b):
        return not (a[-5:].isdigit())

    def clean(self, x):
        return x
