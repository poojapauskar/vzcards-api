from django.db import models
import time
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import RegexValidator

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import random
from random import randint

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

owner = models.ForeignKey('auth.User', related_name='upload_image')
highlighted = models.TextField()

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location=settings.STATIC_ROOT)

class Upload_image(models.Model):
    photo = models.ImageField(null=True, blank=True)
    link=models.TextField(blank=True,default='')



def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.firstname)
    lastname = self.lastname and 'table' or False
    options = self.firstname and {'firstname': self.firstname} or {}
    email = HtmlFormatter(phone=self.phone, lastname=lastname,
                              full=True, **options)
    self.highlighted = highlight(self.email, firstname, formatter)
    super(Upload_image, self).save(*args, **kwargs)