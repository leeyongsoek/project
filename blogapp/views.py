from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import  Question, Choice

# Create your views here.

def index(request):
    return render(request, 'index.html')


def blogMain(request):
    blogs = Blog.objects.all()

    return render(request, 'blogMain.html', {'blogs': blogs})


def createBlog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog_detail': blog_detail})

def new(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'blogapp/new.html', context)

def id(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blogapp/id.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blogapp/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'blogapp/id.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

    # form = CreateBlog()
    #
    # return render(request, 'createBlog.html', {'form': form})