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

owner = models.ForeignKey('auth.User', related_name='ticket')
highlighted = models.TextField()

from django.db import models
import ast


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Ticket(models.Model):
 created = models.DateTimeField(auto_now_add=True)
 vz_id = models.CharField(max_length=100, blank=False)
 user_details = ListField(blank=True, default='',editable=False)
 question = models.CharField(max_length=100, blank=False)
 item = models.CharField(max_length=100, blank=False)
 description = models.TextField()
 #cost = models.CharField(max_length=100, blank=False)
 date_created = models.DateTimeField(auto_now_add=True)
 date_validity = models.DateField(blank=False)
 ticket_id = models.CharField(max_length=100, blank=True,default ='',editable=False)

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