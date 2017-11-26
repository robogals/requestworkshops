from django import forms

from info.models import CHAPTER_LIST, WORKSHOP_TYPE_LIST


class SchoolRequestForm(forms.Form):
	school_name = forms.CharField(max_length=100, required=True)
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)
	mobile = forms.CharField(max_length=100, required=True)
	email = forms.EmailField(required=True)
	school_address = forms.CharField(max_length=100, required=True)
	school_city = forms.CharField(max_length=100, required=True)
	school_postcode = forms.CharField(required=True)
	position = forms.CharField(max_length=100, required=True)
	chapter = forms.ChoiceField(choices=CHAPTER_LIST, required=True)
	workshop_type = forms.ChoiceField(choices=WORKSHOP_TYPE_LIST, required=True)
	permission_to_contact = forms.BooleanField(required=False, initial=True)
	terms = forms.BooleanField(required=True)
