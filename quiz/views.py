from django.shortcuts import render,redirect
from .models import Question,Choice
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator, Page



class LoginPage(LoginView):
    template_name = 'quiz/login.html'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('quizlist')
    

    
class RegisterPage(FormView):
    template_name = 'quiz/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('quizlist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('quizlist')
        return super(RegisterPage, self).get(*args, **kwargs)


class QuizList(ListView):
    model = Question
    fields ='__all__'
    context_object_name = 'questions'
    # set question number showed in a page
    paginate_by = 1
    # custome page object name to 'page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = context['page_obj']
        return context

class QuizDetail(DetailView):
    model = Choice
    fields ='__all__'
    context_object_name = 'choices'










