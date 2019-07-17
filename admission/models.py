# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

ADMISSION_STATUS = (
	('Waiting', 'Waiting'),
	('Approved', 'Approved'),
	('Declined', 'Declined')
	)

GENDER = (
	('Male', 'Male'),
	('Female', 'Female'),
	('Other', 'Other')
	)

RELIGION = (
	('Islam', 'Islam'),
	('Christianity', 'Christianity'),
	('Other', 'Other')
	)


MODES = (
	('DE', 'DE'),
	('UTME', 'UTME'),
	)

CERTIFICATE = (
	('WAEC', 'WAEC'),
	('NECO', 'NECO'),
	('NAPTEB', 'NAPTEB'),
	)

GRADES = (
	('A1', 'A1'),
	('B2', 'B2'),
	('B3', 'B3'),
	('C4', 'C4'),
	('C5', 'C5'),
	('C6', 'C6'),
	('D7', 'D7'),
	('E8', 'E8'),
	('F9', 'F9'),
	)

def get_default_session():
	import datetime
	year = datetime.datetime.today().year
	return "{} / {}".format(year, year+1)


class Session(models.Model):
	session = models.CharField(max_length=30, default=get_default_session())
	current_session = models.BooleanField(default=False)

	def __str__(self):
		return self.session


class OnlineAdmission(models.Model):
	""" A model for onliine admission, it represents a database table, each variable below represents a field in the database table. """
	
	#Applicant Information

	admission_id = models.CharField(max_length=10)
	student_fname = models.CharField(max_length=20)
	student_lname = models.CharField(max_length=20)
	student_oname = models.CharField(max_length=20, blank=True, null=True)
	student_gender = models.CharField(choices=GENDER, max_length=7)
	student_address = models.CharField(max_length=200)
	student_religion = models.CharField(choices=RELIGION, max_length=13)
	student_dob = models.DateField()
	mode_of_entry = models.CharField(max_length=50, choices=MODES)
	applicant_phone_no = models.CharField(max_length=11)
	student_email = models.EmailField(blank=True, null=True)
	date_of_application = models.DateTimeField(auto_now_add=True)
	student_passport = models.ImageField(upload_to="admission/")
	status = models.CharField(max_length=20, default='Waiting', choices=ADMISSION_STATUS)
	session = models.ForeignKey(Session, on_delete=models.CASCADE)

	# Academic histrory
	sec_school_attended = models.CharField(max_length=200)
	sec_from = models.CharField(max_length=200)
	sec_to = models.CharField(max_length=200)
	pri_school_attended = models.CharField(max_length=200)
	pri_from = models.CharField(max_length=200)
	pri_to = models.CharField(max_length=200)
	certificate = models.CharField(max_length=200, choices=CERTIFICATE)

	def get_applicant_full_name(self):
		return "{} {} {}".format(
			self.student_fname or '', 
			self.student_lname or '', 
			self.student_oname or ''
		)

	def __str__(self):
		return "{} ({} {})".format(
			self.admission_id, 
			self.student_fname, 
			self.student_lname
		)

class SubjectGrade(models.Model):
	applicant = models.ForeignKey(OnlineAdmission, on_delete=models.CASCADE)
	subject_name = models.CharField(max_length=200)
	grade = models.CharField(max_length=2, choices=GRADES)
