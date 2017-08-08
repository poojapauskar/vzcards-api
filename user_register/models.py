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

owner = models.ForeignKey('auth.User', related_name='user_register')
highlighted = models.TextField()

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location=settings.STATIC_ROOT)

class User_register(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100, blank=True,default='')
    lastname = models.CharField(max_length=100, blank=True,default='')
    title = models.CharField(max_length=100, blank=True,default='')
    email = models.EmailField(max_length=100, blank=True,default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
    phone = models.CharField(max_length=14,validators=[phone_regex], blank=False) # validators should be a list
    vz_id = models.CharField(blank=True,max_length=15,default='',editable=True)
    otp_generated = models.CharField(blank=True,max_length=15,default='',editable=False)
    industry = models.CharField(max_length=100, blank=True,default='')
    company = models.CharField(max_length=100, blank=True,default='')
    address_line_1 = models.CharField(max_length=100, blank=True,default='')
    address_line_2 = models.CharField(max_length=100, blank=True,default='')
    city = models.CharField(max_length=100, blank=True,default='')
    pin_code = models.CharField(max_length=6,blank=True,default='')
    token_generated = models.TextField(blank=True,default='')
    photo = models.TextField(blank=True,default='')
    company_photo = models.TextField(blank=True,default='')
    reference_code = models.CharField(max_length=100, blank=True,default=1)
    is_organization = models.CharField(max_length=100, blank=True,default='')
    otp_created_time = models.CharField(blank=True,max_length=100,default='',editable=True)
   # photo = models.ImageField(upload_to="projectimg/",storage=fs, null=True, blank=True)
    
    
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
    super(User_register, self).save(*args, **kwargs)