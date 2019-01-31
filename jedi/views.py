from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, reverse
# from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView

from .forms import CandidateForm, TestForm
from .models import Jedi, Candidate, Planet, Test


def main(request):
    return render_to_response('main.html')


class JediView(generic.ListView):
    template_name = 'jedi.html'
    context_object_name = 'jedi_list'

    def get_queryset(self):
        return Jedi.objects.all()


class ListOfCandsView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'candidates_list'

    def get_queryset(self):
        # return Candidate.objects.all()
        return Candidate.objects.filter(homeplanet=Jedi.edu_planet)


class ResumeView(FormView):
    form_class = CandidateForm
    template_name = 'resume.html'

    def post(self, request):
        form = CandidateForm(self.request.POST)
        if form.is_valid():
            candidate = form.save()
            return HttpResponseRedirect(reverse('jedi:test', args=(candidate.id,)))
        return self.render_to_response({'form': form})


class TestView(FormView):
    form_class = TestForm
    template_name = 'test.html'

    def post(self, request):
        form = TestForm(self.request.POST)
        if form.is_valid():
            test = form.save()
            return HttpResponseRedirect(reverse('jedi:thanks'))
        return self.render_to_response('test.html')


def thanks(request):
    return render_to_response('thanks.html')
