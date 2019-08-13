from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from django.core.mail import EmailMessage

from core.models import Recruit, ShadowHandQuestion, QuestionChoice, Sith


def index_redirect(request):
    return HttpResponseRedirect(reverse('core:main'))


class CongratulationsView(generic.TemplateView):
    template_name = 'core/congratulations.html'


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'


class CreateRecruitView(generic.CreateView):
    template_name = 'core/create_recruit.html'
    model = Recruit
    fields = '__all__'

    def form_valid(self, form):
        recruit = form.save()
        self.request.session['recruit_id'] = recruit.id
        return HttpResponseRedirect(reverse('core:recruit_questions'))


class Questions(generic.ListView):
    template_name = 'core/questions.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return ShadowHandQuestion.objects.all()

    def post(self, request):
        questions = ShadowHandQuestion.objects.all()
        rec_id = self.request.session['recruit_id']
        recruit = Recruit.objects.get(id=rec_id)
        for question in questions:
            QuestionChoice.objects.create(task=question,
                                          choice_text=self.request.POST['answer-%d' % question.id],
                                          voted=recruit)
        return HttpResponseRedirect(reverse('core:congratulations'))


class SithsListView(generic.ListView):
    template_name = 'core/siths_list.html'
    context_object_name = 'siths_list'

    def get_queryset(self):
        return Sith.objects.all()

    def post(self, request):
        self.request.session['sith_name'] = self.request.POST['sith-id']
        return HttpResponseRedirect(reverse('core:all_recruits'))


class SithsShortcutListView(generic.ListView):
    template_name = 'core/siths_list_shortcut.html'
    context_object_name = 'siths_list'

    def get_queryset(self):
        return Sith.objects.all()


class RecruitDetailView(generic.DetailView):
    template_name = 'core/recruit_detail.html'
    model = Recruit
    context_object_name = 'recruit'

    def get_queryset(self):
        return Recruit.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recruit_answers'] = QuestionChoice.objects.filter(voted__in=self.get_queryset())
        return context


class RecruitsListView(generic.ListView):
    template_name = 'core/recruits_list.html'
    context_object_name = 'rec_list'

    def get_queryset(self):
        return Recruit.objects.all()

    def post(self, request):
        choices = request.POST.getlist('recruit-id')
        sith_name = request.session['sith_name']
        sith = Sith.objects.get(name=sith_name)
        if (len(choices) + sith.padavans.count()) > 3:
            return render(request, 'core/notify.html',
                          {'error': 'К сожалению не можете иметь больше 3х падаванов, господин',
                           'message': 'Что-то пошло не так'})
        else:
            for choice in choices:
                recruit = Recruit.objects.get(id=choice)
                sith.padavans.add(recruit)
                sith.save()
                email = self.generate_email(sith, recruit)
                email.send()
            return render(request, 'core/notify.html',
                          {'message': 'Успех! Рекрут оповещен и зачислен в ряды Рук Смерти!'})

    def generate_email(self, sith, recruit):
        email_message = EmailMessage('Поздравляем, теперь у тебя есть сенсей',
                                     'Лорд %s согласился взять тебя в ученики' % sith.name,
                                     to=[recruit.email])
        return email_message
