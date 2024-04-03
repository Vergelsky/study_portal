import re
from rest_framework.validators import ValidationError


class CorrectLinkValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        for field in self.fields:
            tmp_val = dict(value).get(field)
            if tmp_val:
                if 'http' in tmp_val and not 'youtube.com' in tmp_val:
                    raise ValidationError("Ссылки на ресурсы кроме youtube запрещены")
