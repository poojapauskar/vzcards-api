from django.db import models
import random
from random import randint
# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight



LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

owner = models.ForeignKey('auth.User', related_name='ticket_create')
highlighted = models.TextField()



class Ticket_create(models.Model):
 created = models.DateTimeField(auto_now_add=True)
 vz_id = models.CharField(max_length=100, blank=False)
 user_details = models.TextField(blank=True,default ='')
 question = models.CharField(max_length=100, blank=False)
 item = models.CharField(max_length=100, blank=False)
 description = models.TextField()
 #cost = models.CharField(max_length=100, blank=False)
 date_created = models.DateTimeField(auto_now_add=True)
 date_validity = models.DateField(blank=False)
 ticket_id = models.CharField(max_length=100, blank=True,default ='',editable=False)
 item_photo= models.TextField(blank=True,default ='')

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