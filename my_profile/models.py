from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.core.validators import RegexValidator

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

owner = models.ForeignKey('auth.User', related_name='user_register')
highlighted = models.TextField()

class My_profile(models.Model):
 created = models.DateTimeField(auto_now_add=True) # validators should be a list
 phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
 phone = models.CharField(max_length=14,validators=[phone_regex], blank=False,default='') # validators should be a list
 vz_id = models.CharField(blank=True,max_length=15,default='',editable=True)
 firstname = models.CharField(max_length=100, blank=True,default='')
 lastname = models.CharField(max_length=100, blank=True,default='')
 email = models.EmailField(max_length=100, blank=True,default='')
 industry = models.CharField(max_length=100, blank=True,default='')
 company = models.CharField(max_length=100, blank=True,default='')
 address_line_1 = models.CharField(max_length=100, blank=True,default='')
 address_line_2 = models.CharField(max_length=100, blank=True,default='')
 city = models.CharField(max_length=100, blank=True,default='')
 pin_regex = RegexValidator(regex=r'^\+?1?\d{6}$', message="Enter 6 digit pin code.")
 pin_code = models.CharField(max_length=6,validators=[pin_regex], blank=True,default='')
 photo = models.TextField(blank=True,default='')

 class Meta:
  ordering = ('created',)

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