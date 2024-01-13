from django.urls import path 
from .views import QuizList, QuizDetail,LoginPage,RegisterPage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', LoginPage.as_view(), name="login"),
    path('register/', RegisterPage.as_view(), name="register"),

    path('', QuizList.as_view(), name="quizlist"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)