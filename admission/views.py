# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Session, OnlineAdmission, SubjectGrade

import string
import random
def admissionNumberCodeGen():
	counter = OnlineAdmission.objects.all().count()
	admission_no = "#{0:03}".format(counter+1)
	return admission_no

def home(request):
	session = Session.objects.get(current_session=True)
	context = {
		'session': session
	}
	return render(request, 'online_admission/home.html', context)

def save_application(request):
	application = request.POST
	fname = application.get('fname')
	sname = application.get('sname')
	oname = application.get('oname')
	gender = application.get('gender')
	religion = application.get('religion')
	dob = application.get('dob')
	mode = application.get('mode_of_entry')
	phone_no = application.get('phone_no')
	email = application.get('email')
	certificate = application.get('certificate')
	sec_att = application.get('sec_attended')
	pri_att = application.get('pri_attended')
	sec_from = application.get('sec_from')
	sec_to = application.get('sec_to')
	pri_from = application.get('pri_from')
	pri_to = application.get('pri_to')

	applicant = OnlineAdmission.objects.create(
		student_fname=fname,
		student_lname=sname,
		student_oname=oname,
		student_gender=gender,
		student_religion=religion,
		student_dob=dob,
		mode_of_entry=mode,
		applicant_phone_no=phone_no,
		student_email=email,
		session=Session.objects.get(current_session=True),
		sec_school_attended=sec_att,
		pri_school_attended=pri_att,
		pri_from=pri_from,
		sec_from=sec_from,
		sec_to=sec_to,
		pri_to=pri_to,
		certificate=certificate,
		admission_id=admissionNumberCodeGen())
	
	#subjects
	eng = application.get('s1')
	eng_grade = application.get('s1_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=eng,
		grade=eng_grade
	)

	math = application.get('s2')
	math_grade = application.get('s2_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=math,
		grade=math_grade
	)

	s3 = application.get('s3')
	s3_grade = application.get('s3_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=s3,
		grade=s3_grade
	)

	s4 = application.get('s4')
	s4_grade = application.get('s4_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=s4,
		grade=s4_grade
	)

	s5 = application.get('s5')
	s5_grade = application.get('s5_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=s5,
		grade=s5_grade
	)
		
	s6 = application.get('s6')
	s6_grade = application.get('s6_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=s6,
		grade=s6_grade
	)

	s7 = application.get('s7')
	s7_grade = application.get('s7_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=s7,
		grade=s7_grade
	)
	
	s8 = application.get('s8')
	s8_grade = application.get('s8_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=s8,
		grade=s8_grade
	)
	
	s9 = application.get('s9')
	s9_grade = application.get('s9_grade')
	SubjectGrade.objects.create(
		applicant=applicant,
		subject_name=s9,
		grade=s9_grade
	)
	
	del request.session['code']
	request.session['code'] = applicant.admission_id
	return redirect('/#success')


def search_admission(request):
	if request.is_ajax():
		q = request.GET.get('data')
		if OnlineAdmission.objects.filter(admission_id=q).exists():
			q = OnlineAdmission.objects.get(admission_id=q)
			message = "Hello {}, \
			Your Admission Status is: \
			<span style='background-color: green; \
			padding: 10px; margin:10px;'>{}</span>".format(q.get_applicant_full_name(), q.status)
		else:
			message = "Sorry !, We coul'nt find an application with application number {}".format(q)
		return HttpResponse(message)
	else:
		return redirect('/')