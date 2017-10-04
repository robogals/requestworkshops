from django.shortcuts import render

from info.forms import SchoolRequestForm
from info.models import SchoolRequestInformation, CHAPTER_LIST

import logging

logging.basicConfig(filename='views.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# TODO: Things on my list...
# 5. Need to deploy onto myrobogals instance
# 6. Need to be able to integrate into myrobogals db and send emails (cronjob with django python script to save to DB)
# 7. Admin interface to view metrics (using graph.js)
# 9. Clean up code


def home(request):
	request_form = SchoolRequestForm(request.POST or None)
	logging.debug(request)

	if request.method == 'POST':
		logging.debug('Posted')

		if request_form.is_valid():
			logging.debug('Form past checks')
			v = SchoolRequestInformation()
			v.school_name = request_form.cleaned_data['school_name']
			v.first_name = request_form.cleaned_data['first_name']
			v.last_name = request_form.cleaned_data['last_name']
			v.mobile = request_form.cleaned_data['mobile']
			v.email = request_form.cleaned_data['email']
			v.school_address = request_form.cleaned_data['school_address']
			v.school_city = request_form.cleaned_data['school_city']
			v.school_postcode = request_form.cleaned_data['school_postcode']
			v.position = request_form.cleaned_data['position']
			v.chapter = request_form.cleaned_data['chapter']
			v.permission_to_contact = request_form.cleaned_data['permission_to_contact']

			v.save()

			logging.debug('Returning success screen')
			return render(request, 'success.html', {'chapter': [y for x, y in CHAPTER_LIST if x == int(v.chapter)][0]})
		else:
			logging.debug('Form failed %s', request_form)

	return render(request, 'home.html', {'form': request_form})