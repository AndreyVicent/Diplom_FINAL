from django.urls import path
from . import views
from .views import get_subscriptions
from .views import trainings_api
from .views import workouts_api
from django.urls import path
from .views import register_view, login_view, logout_view, profile_view


urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('index4/', views.index4, name='index4'),
    path('index5/', views.index5, name='index5'),
    path('index6/', views.index6, name='index6'),
    path('get_subscriptions/', get_subscriptions, name='get_subscriptions'),
    path('api/trainings/', trainings_api, name='trainings_api'),
    path('api/workouts/', workouts_api, name='workouts_api'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('callback/', views.callback_request, name='callback'),
    path('subscription-request/', views.subscription_request, name='subscription_request'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]



