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

owner = models.ForeignKey('auth.User', related_name='connect')
highlighted = models.TextField()

class Connect(models.Model):
 connecter_vz_id = models.CharField(max_length=100, blank=True, default='')
 phone_1 = models.CharField(max_length=100, blank=True, default='')
 ticket_id_1 = models.CharField(max_length=100, blank=True, default='')
 phone_2 = models.CharField(max_length=100, blank=True, default='')
 ticket_id_2 = models.CharField(max_length=100, blank=True, default='')
 


def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.connecter_vz_id)
    phone_1 = self.phone_1 and 'table' or False
    ticket_id_1 = self.connecter_vz_id and {'connecter_vz_id': self.connecter_vz_id} or {}
    description = HtmlFormatter(phone_2=self.phone_2, ticket_id_2=ticket_id_2,
                              full=True, **options)
    self.highlighted = highlight(self.ticket_id_1,connecter_vz_id, formatter)
    super(Create, self).save(*args, **kwargs)