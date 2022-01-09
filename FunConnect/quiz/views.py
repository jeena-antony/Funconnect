from django.contrib.auth.models import User
from django.core import paginator
from django.db.models.fields.related import ForeignKey
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from quiz import forms
from quiz.forms import GameForm, MarksForm, QuestionForm
from quiz.models import game, mark, question
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    game_list=game.objects.all()
    context={
        'game_list':game_list,
    }
    # return HttpResponse("<H1> This is index </H1>")
    return render(request,'quiz/index.html',context)

@login_required
def detail(request,game_id):
    game_id=game.objects.get(pk=game_id)
    # game=game.objects.get(pk=game_id)
    context={
            'game_id':game_id
        }
    return render(request,'quiz/detail.html',context)
@login_required
def create_game(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/quiz')

    return render(request,'quiz/game-form.html',{'form':form}) 
        
@login_required
def update_game(request,id):
    game_item=game.objects.get(id=id)
    form =GameForm(request.POST or None ,instance=game_item)
    if form.is_valid():
        form.save()
        return redirect('/quiz')
    
    return render(request,'quiz/game-form.html',{'form':form,'game_item':game_item})

@login_required
def delete_game(request,id):
    game_item=game.objects.get(id=id)

    if request.method== 'POST':
        game_item.delete()
        return redirect('/quiz')

    return render(request,'quiz/game-delete.html',{'game_item':game_item})


@login_required
def start_game(request,id):
    game_id=game.objects.get(pk=id)
    question_id=question.objects.filter(game_id=game_id)
    context={
            'game_id':game_id,
            'question_id':question_id,
        }
    return render(request,'quiz/start-game.html',context)


@login_required
def questionpage(request,id):
    question_id=question.objects.filter(game_id=id)
    user =request.user
    marks=mark.objects.filter(game_id=id).filter(user_id=user.id)
    marks_id=marks[0]
    print(marks[0].id ,"marks value" )
    form =QuestionForm()
    print(question_id)
    paginator =Paginator(question_id,1)
    page =request.GET.get('page')
    question_id= paginator.get_page(page)
    context={
            'question_id':question_id,
            'form':form,
            'marks_id':marks_id,
        }
    
    if request.method == 'POST':

        answer=request.POST.get('answer')
        option=request.POST.get('options')
        nextpage=request.POST.get('nextpage')
        if answer==option:
            userr = request.user
            user=User.objects.get(pk=userr.id)
            gamee=request.POST.get('game_id')
            gamez=game.objects.get(pk=gamee)
            marks=10
            mark_object=mark.objects.filter(game_id=gamez).filter(user_id=user)
            print(mark_object,'mark object')
            if mark_object :
                print("insdie if",type(marks))
                # mark_object.update(mark=(mark)+10) 
                mark_object[0].mark=mark_object[0].mark +10
                mark_object[0].save()
                 
            else:
                mark_object= mark(user_id=user,game_id=gamez,mark=10)
                mark_object.save()      
            messages.success(request,' answer is correct')         
        else:
            messages.warning(request,' answer is wrong')
    
    return render(request,'quiz/question.html',context)
        
     

@login_required
def marks_page(request):
    answer=request.POST.get('options')
    print(answer, "answer")
    marks_id=mark.objects.all()
    current_user = request.user
    form =QuestionForm()
    print(current_user.id)
    context={
            'marks_id':marks_id,
            'form':form,
            'current_user':current_user
        }
    return render(request,'quiz/marks.html',context)

@login_required
def result(request,id):
    current_user = request.user
    marks_id=mark.objects.filter(game_id=id).filter(user_id=current_user.id)
    context={
        'marks_id':marks_id,
    }
    return render(request,'quiz/result.html',context)

@login_required
def correct_answer(request):
    context={
    }
    return render(request,'quiz/correct-answer.html',context)
    
@login_required
def wrong_answer(request):
    context={
    }
    return render(request,'quiz/wrong-answer.html',context)

@login_required
def answer_page(request):
    answer=request.POST.get('answer')
    option=request.POST.get('options')
    nextpage=request.POST.get('nextpage')
        
    print(type(answer),'answer type')
    print(type(nextpage),'nextpage type')
    if answer==option:
        result=True
        # user = request.POST.get('user_id')
        # game=request.POST.get('game_id')
        # marks=10
        # print("successs")
        # mark_object= mark(user_id=user,game_id=game,mark=marks)
        # print(mark_object,"mark_object")
        # mark_object.save()
    else:
        result=False
    context={
        'result':result,
        'nextpage':nextpage,
        'game_id':game,

    }
    return render(request,'quiz/answer.html',context)
    
@login_required
def home_page(request):
    context={
    }
    return render(request,'quiz/home.html',context)