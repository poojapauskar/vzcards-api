from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

owner = models.ForeignKey('auth.User', related_name='friends')
highlighted = models.TextField()

class Friends(models.Model):
 vz_id = models.CharField(max_length=100, blank=True, default='')
 friends_vz_id = models.CharField(max_length=100, blank=True, default='')
 
 

def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.vz_id)
    contacts = self.contacts and 'table' or False
    contacts = self.vz_id and {'vz_id': self.vz_id} or {}
   
    self.highlighted = highlight(self.contacts,vz_id, formatter)
    super(Friends, self).save(*args, **kwargs)