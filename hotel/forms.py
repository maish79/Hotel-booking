from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
            ('single', 'one'),
            ('double', 'two'),
            ('family','multi'),
    )

    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=("%Y%m%d-%H%M%S"))
    check_out = forms.DateTimeField(required=True, input_formats=("%Y%m%d-%H%M%S"))