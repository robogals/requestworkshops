from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from info.forms import SchoolRequestForm
from info.models import SchoolRequestInformation, CHAPTER_LIST

# import logging
# logging.basicConfig(filename='views.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def home(request):
	request_form = SchoolRequestForm(request.POST or None)

	if request.method == 'POST':
		if request_form.is_valid():
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

			return HttpResponseRedirect(reverse('success'))
	print request_form['chapter']
	return render(request, 'home.html', {'form': request_form})


def success(request):
	v = SchoolRequestInformation.objects.order_by('-id')[0]
	chapter = [y for x, y in CHAPTER_LIST if x == int(v.chapter)][0]
	return render(request, 'success.html', {'chapter': chapter})
