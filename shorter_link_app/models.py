from django.db import models
from django.db import models
from django.db import models
import string
from math import floor


class Link(models.Model):
    link = models.URLField()

    # Base62 Encoder
    # toBase62
    def get_short_id(self, b=62):
        num = self.id

        if b <= 0 or b > 62:
            return 0
        base = string.digits + string.ascii_lowercase + string.ascii_uppercase
        r = num % b
        res = base[r]
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    # Base62 Decoder
    # toBase10
    @staticmethod
    def decode_id(num, b=62):
        base = string.digits + string.ascii_lowercase + string.ascii_uppercase
        limit = len(num)
        res = 0
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res
