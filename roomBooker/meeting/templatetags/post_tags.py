from django import template
from datetime import datetime, timedelta
from meeting.models import Meet

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
    dates_of_week = [date.strftime('%d.%m.%Y') for date in dates_of_week]
    return dates_of_week


@register.simple_tag
def range_values():
    return [f"{hour:02d}:{min:02d}" for hour in range(24) for min in [0, 30]]


@register.simple_tag
def dict_of_dates_and_hours():
    meet_data = {}
    meets = Meet.objects.all()
    for meet in meets:
        start_time = datetime.combine(datetime.today(), meet.start_time).time()
        end_time = datetime.combine(datetime.today(), meet.end_time).time()
        time_list = []
        current_time = datetime.combine(datetime.today(), start_time)

        while current_time.time() <= end_time:
            time_list.append(current_time.strftime('%H:%M'))
            current_time += timedelta(minutes=30)

        date_key = meet.meet_date.strftime('%d.%m.%Y')
        if date_key in meet_data:
            meet_data[date_key].extend(time_list)
        else:
            meet_data[date_key] = time_list

    return meet_data


@register.simple_tag
def get_meet_times(meets, date):
    """
    zastępuje meets.get(date), co w szablonach jest niedozwolone
    """
    return meets.get(date)
