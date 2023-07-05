from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.simple_tag(name='get_current_date')
def get_current_date():
    current_date = datetime.now().date()
    return current_date


@register.simple_tag()
def actual_week():
    current_date = datetime.now().date()

    # Wyznaczanie numeru dnia tygodnia (poniedziałek - 0, wtorek - 1, ..., niedziela - 6)
    day_of_week = current_date.weekday()

    # Wyznaczanie daty początku i końca bieżącego tygodnia
    start_of_week = current_date - timedelta(days=day_of_week)

    # Generowanie pozostałych dat dla obecnego tygodnia
    dates_of_week = [start_of_week + timedelta(days=i) for i in range(7)]

    return dates_of_week


@register.simple_tag
def range_values():
    return [f"{hour:02d}:{min:02d}" for hour in range(24) for min in [0, 30]]