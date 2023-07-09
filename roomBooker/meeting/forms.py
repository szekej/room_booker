from django import forms
from .models import Meet


class CreateMeetForm(forms.ModelForm):
    start_time = forms.ChoiceField(choices=[(f"{hour:02d}:{min:02d}", f"{hour:02d}:{min:02d}") for hour in range(24) for min in [0, 30]])
    end_time = forms.ChoiceField(choices=[(f"{hour:02d}:{min:02d}", f"{hour:02d}:{min:02d}") for hour in range(24) for min in [0, 30]])
    meet_date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(2023, 2030)  # zakres lat do wyboru
        )
    )

    class Meta:
        model = Meet
        exclude = ('user', )
