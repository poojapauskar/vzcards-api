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

owner = models.ForeignKey('auth.User', related_name='register')
highlighted = models.TextField()

class Register(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
    phone = models.CharField(max_length=12,validators=[phone_regex], blank=False) # validators should be a list
    vz_id = models.CharField(blank=True,max_length=15,default='',editable=True)
    otp_generated = models.CharField(blank=True,max_length=15,default='',editable=False)
    industry = models.CharField(max_length=100, blank=True,default='')
    address_line_1 = models.CharField(max_length=100, blank=True,default='')
    address_line_2 = models.CharField(max_length=100, blank=True,default='')
    city = models.CharField(max_length=100, blank=True,default='')
    pin_regex = RegexValidator(regex=r'^\+?1?\d{6}$', message="Enter pin code.")
    pin_code = models.CharField(max_length=6,validators=[pin_regex], blank=True,default='')
    
    
    class Meta:
        ordering = ('created',)

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
    super(Register, self).save(*args, **kwargs)