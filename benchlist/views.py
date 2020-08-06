from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
def consultants_view(request):
    context = {}
    form = forms.ConsultantForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    context['form'] = forms.ConsultantForm()
    context['consultants'] = models.Consultant.objects.all()
    context['active'] = '1'
    # models.Consultant.objects.all().delete()
    return render(request, 'consultants.html', context)

def prospect_consultants_view(request):
    context = {}
    form = forms.ProspectConsultantForm(request.POST) 
    if request.method == 'POST':
        form.save()
    context['form'] = forms.ProspectConsultantForm()
    context['consultants'] = models.ProspectConsultant.objects.all()
    context['active'] = '2'

    # models.ProspectConsultant.objects.all().delete()
    return render(request, 'prospect_consultants.html', context)

def benchlist_view(request):
    context = {}
    form = forms.BenchlistForm(request.POST) 
    if request.method == 'POST':
        form.save()
    context['form'] = forms.BenchlistForm()
    context['consultants'] = models.Benchlist.objects.all()
    context['active'] = '3'

    # models.Benchlist.objects.all().delete()
    return render(request, 'benchlist.html', context)


def submission_view(request):
    context = {}
    form = forms.SubmissionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        obj = form.save(commit=False)
        state = data.get('client_state')
        status = data.get('submission_status')
        for each in models.STATES:
            for i in each:
                if i == state:
                    obj.client_state = each[1]  
        for each in models.STATUS:
            for i in each:
                if i == status:
                    obj.submission_status = each[1]  
        obj.save()
    context['form'] = forms.SubmissionForm()
    context['submissions'] = models.Submission.objects.all()
    context['active'] = '4'
    # models.Submission.objects.all().delete()
    return render(request, 'submissions.html', context)


def home_view(request):
    context = {}
    return render(request, 'base.html', context)
