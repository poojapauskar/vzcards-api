from django.db import models

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

owner = models.ForeignKey('auth.User', related_name='connect')
highlighted = models.TextField()

class Connect(models.Model):
 connecter_vz_id = models.CharField(max_length=100, blank=True, default='')
 #connecter_details=models.TextField(blank=True, default='')
 phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
 phone_1 = models.CharField(max_length=12,validators=[phone_regex], blank=False)
 ticket_id_1 = models.CharField(max_length=100, blank=True, default='')
 phone_2 = models.CharField(max_length=12,validators=[phone_regex], blank=False)
 ticket_id_2 = models.CharField(max_length=100, blank=True, default='')
 reffered_phone = models.CharField(max_length=12,validators=[phone_regex], blank=True)
 reffered_ticket = models.CharField(max_length=100, blank=True, default='')
 my_ticket =models.CharField(max_length=100, blank=True, default='')
 #ticket_1_details=models.TextField(blank=True, default='')
 #ticket_2_details=models.TextField(blank=True, default='')
 #phone_1_details=models.TextField(blank=True, default='')
 #phone_2_details=models.TextField(blank=True, default='')
 #ticket_1_dates=models.TextField(blank=True, default='')
 #ticket_2_dates=models.TextField(blank=True, default='')


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