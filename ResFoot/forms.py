from django import forms

class CalendarForm(forms.Form):
    selected_date = forms.DateField()
