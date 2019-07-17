# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import OnlineAdmission, Session, SubjectGrade

class SessionAdmin(admin.ModelAdmin):
	"""docstring for SessionAdmin"""

	list_display = ['session']
	search_fields = ['session']


def accept_selected(modeladmin, request, queryset):
	queryset.update(status='Approved')
accept_selected.short_description = "Admit selected applicant"

def put_selected_on_waiting(modeladmin, request, queryset):
    queryset.update(status='Waiting')
put_selected_on_waiting.short_description = "Put selected applicant on waiting list"


def reject_selected(modeladmin, request, queryset):
    queryset.update(status='Declined')
reject_selected.short_description = "Reject selected applicant"


class OnlineAdmissionAdmin(admin.ModelAdmin):
	list_filter = ['status', 'mode_of_entry']
	list_display = [
		'admission_id',
		'student_fname', 
		'student_lname', 
		'student_oname', 
		'student_gender', 
		'mode_of_entry',
		'status',
		'applicant_phone_no',
		'student_email',
		'student_address',
	]

	search_fields = (
		'admission_id', 
		'mode_of_entry', 
		'status', 
		'student_fname', 
		'student_email'
	)

	fieldsets = (
        ('Applicant Information', {
            'fields': (
            	'admission_id', 
            	'student_fname', 
            	'student_lname', 
            	'mode_of_entry',
            	'applicant_phone_no',
            	'status',
            )
        }),

        ('Education History', {
            'fields': ('certificate','pri_school_attended', 'pri_from', 'pri_to', 'sec_school_attended', 'sec_from', 'sec_to'),
        }),

        ('Optional Fields', {
        	'classes': ('collapse',),
            'fields': ('student_oname', 'student_email',)
        }),

        ('Other Information', {
            'fields': ('session', 'student_dob'),
        }),
    )
	actions = [accept_selected, put_selected_on_waiting, reject_selected]

admin.site.register(OnlineAdmission, OnlineAdmissionAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(SubjectGrade)
admin.site.site_header = 'Mautech Online Admission'

from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)