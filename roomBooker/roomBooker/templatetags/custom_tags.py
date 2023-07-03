from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.simple_tag(name='get_current_date')
def get_current_date():
    current_date = datetime.now().date()
    return current_date
