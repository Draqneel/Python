from django.urls import path, include
from core.views import IndexView, CreateRecruitView, Questions, CongratulationsView, SithsListView, RecruitsListView, \
    SithsShortcutListView, RecruitDetailView

app_name = 'core'

urlpatterns = [
    path('main/', IndexView.as_view(), name='main'),
    path('create/rec/', CreateRecruitView.as_view(), name='create_rec'),
    path('create/rec/questions/', Questions.as_view(), name='recruit_questions'),
    path('create/rec/congratulations/', CongratulationsView.as_view(), name='congratulations'),
    path('choose/sith/', SithsListView.as_view(), name='all_siths'),
    path('choose/sith/recruit/<int:pk>/', RecruitDetailView.as_view(), name='rec_detail'),
    path('choose/sith/shortcut', SithsShortcutListView.as_view(), name='all_siths_shortcut'),
    path('choose/sith/recruit', RecruitsListView.as_view(), name='all_recruits'),
]
