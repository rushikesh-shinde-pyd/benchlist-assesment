from django import forms
from . import models

class ConsultantForm(forms.ModelForm):
    """Form definition for ConsultantForm."""

    class Meta:
        """Meta definition for ConsultantForm."""

        model = models.Consultant
        fields = "__all__"


class ProspectConsultantForm(forms.ModelForm):
    """Form definition for ProspectConsultantForm."""

    class Meta:
        """Meta definition for ProspectConsultantFormform."""

        model = models.ProspectConsultant
        fields = '__all__'


class BenchlistForm(forms.ModelForm):
    """Form definition for BenchlistForm."""

    class Meta:
        """Meta definition for BenchlistFormform."""

        model = models.Benchlist
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class SubmissionForm(forms.ModelForm):
    """Form definition for SubmissionForm."""
    date_of_submission = forms.DateField(widget=DateInput(), help_text='*')
    consultant_name = forms.CharField(widget=forms.TextInput(), help_text='*')
    job_title = forms.CharField(widget=forms.TextInput(), help_text='*')
    rate = forms.DecimalField(help_text='*', required=False)
    client = forms.CharField(widget=forms.TextInput(), help_text='*')
    client_city = forms.CharField(widget=forms.TextInput(), help_text='*')
    client_state = forms.ChoiceField(widget=forms.Select(), help_text='*', choices=models.STATES)
    vendor_company = forms.CharField(help_text='*')
    vendor_recruiter_contact = forms.CharField(help_text='*')
    vendor_location = forms.CharField(help_text='*')
    submission_status = forms.ChoiceField(widget=forms.Select(), help_text='*', choices=models.STATUS)
    reason = forms.CharField(required=False, widget=forms.Textarea(attrs = {
        'disabled': True,
        'rows': '5'
    }))
    note = forms.CharField(required=False, widget=forms.Textarea(attrs = {
        'disabled': True,
        'rows': '5'
    }))


    class Meta:
        """Meta definition for SubmissionForm."""

        model = models.Submission
        fields = '__all__'

