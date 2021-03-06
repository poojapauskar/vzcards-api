from django.db import models
import random
from random import randint
# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import RegexValidator

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

owner = models.ForeignKey('auth.User', related_name='verify')
highlighted = models.TextField()

class Verify(models.Model):
 phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Enter country code. Phone number must be entered in the format: '+919999999'.")
 phone = models.CharField(max_length=12,validators=[phone_regex], blank=False) # validators should be a list
 otp = models.CharField(max_length=100, blank=False,editable=True)
 valid = models.CharField(blank=True,max_length=2,default='',editable=False)
 token_generated = models.TextField(blank=True,default='')
 vz_id=models.TextField(blank=True,default='')



def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.vz_id)
    question = self.question and 'table' or False
    item = self.vz_id and {'vz_id': self.vz_id} or {}
    description = HtmlFormatter(cost=self.cost, date_validity=date_validity,
                              full=True, **options)
    self.highlighted = highlight(self.item,vz_id, formatter)
    super(Create, self).save(*args, **kwargs)