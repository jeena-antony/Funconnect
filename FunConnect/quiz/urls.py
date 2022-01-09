from . import views
from django.urls import path
urlpatterns = [
    path('',views.home_page,name='home'),
    path('index',views.index,name='index'),
    path('<int:game_id>/',views.detail,name='detail'),
    #add
    path('add',views.create_game,name='create_item'),
    #edit
    path('update/<int:id>',views.update_game,name='update_game'),
    #delete
    path('delete/<int:id>',views.delete_game,name='delete_game'),
    path('question/<int:id>',views.questionpage,name='question'),
    path('game/<int:id>',views.start_game,name='start_game'),
    path('marks',views.marks_page,name='marks'),
    path('results/<int:id>',views.result,name='result'),
    path('correct',views.correct_answer,name='correct_answer'),
    path('wrong',views.wrong_answer,name='wrong_answer'),
    path('answer',views.answer_page,name='answer'),
    path('home',views.home_page,name='home'),
]