from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Subscription
from .models import PersonalTraining
from .models import GroupWorkout
from .forms import ReviewForm
from .models import Review
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import SignUpForm
from .models import TrainingSignUp, PersonalTraining, GroupWorkout
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import CallbackForm 
from .models import CallbackRequest  
from django.http import JsonResponse
from .models import SubscriptionRequest 
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime  
from .models import SubscriptionRequest  
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from .models import SubscriptionPayment
import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import UserProfile





def index(request):
    return render(request, 'mainfitnes/index.html')

def index2(request):
    return render(request, 'mainfitnes/index2.html') 

def index3(request):
    return render(request, 'mainfitnes/index3.html') 

def index4(request):
    return render(request, 'mainfitnes/index4.html') 

def index5(request):
    return render(request, 'mainfitnes/index5.html') 

def index6(request):
    return render(request, 'mainfitnes/index6.html') 

def get_subscriptions(request):
    branch = request.GET.get('branch', 'dvor')
    subscriptions = Subscription.objects.filter(
        branch=branch, 
        is_active=True
    ).values('title', 'price', 'duration', 'features')
    
    return JsonResponse(list(subscriptions), safe=False)

def trainings_api(request):
    trainings = PersonalTraining.objects.filter(is_active=True).values(
        'id',
        'sessions',
        'trainer_type',
        'price',
        'description'
    )
    return JsonResponse(list(trainings), safe=False)



def workouts_api(request):
    workouts = GroupWorkout.objects.filter(is_active=True).values(
        'id',
        'title',
        'branch',
        'trainer',
        'description',
        'time',
        'days'
    )
    return JsonResponse(list(workouts), safe=False)


def index5(request):
    reviews = Review.objects.all().order_by('-created_at')  
    form = ReviewForm(request.POST or None) 

    if request.method == 'POST' and form.is_valid():  
        form.save()  
        return redirect('index5')  

    return render(request, 'mainfitnes/index5.html', {
        'form': form,
        'reviews': reviews,
    })



def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            signup = TrainingSignUp(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                training_type=form.cleaned_data['training_type'],
                training_id=form.cleaned_data['training_id']
            )
            signup.save()
            

            if form.cleaned_data['training_type'] == 'personal':
                training = PersonalTraining.objects.get(id=form.cleaned_data['training_id'])
                training_info = f"Персональная тренировка ({training.get_trainer_type_display()}), {training.sessions} занятий"
            else:
                training = GroupWorkout.objects.get(id=form.cleaned_data['training_id'])
                training_info = f"Групповая тренировка: {training.title}, тренер: {training.trainer}"
            

            send_mail(
                'Новая запись на тренировку в BodyClub',
                f"""Поступила новая запись на тренировку:
                
                Имя: {form.cleaned_data['name']}
                Телефон: {form.cleaned_data['phone']}
                Email: {form.cleaned_data['email'] or 'не указан'}
                
                Тренировка: {training_info}
                ID: {form.cleaned_data['training_id']}
                Тип: {form.cleaned_data['training_type']}
                
                Дата записи: {signup.created_at.strftime('%d.%m.%Y %H:%M')}
                """,
                'noreply@bodyclub.ru',  
                ['your@email.com'],     
                fail_silently=False,
            )
            
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Неверный метод запроса'})


def callback_request(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if not form.is_valid():
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })

        try:

            callback = CallbackRequest.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone']
            )


            send_mail(
                'Новая заявка на звонок',
                f'''Данные клиента:
                Имя: {form.cleaned_data['name']}
                Телефон: {form.cleaned_data['phone']}
                Дата: {callback.created_at.strftime('%d.%m.%Y %H:%M')}''',
                'vicentseas@gmail.com',
                ['vicentseas@gmail.com'],
                fail_silently=False
            )

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({
                'success': False,
                'errors': str(e)
            })

    return JsonResponse({
        'success': False,
        'errors': 'Разрешены только POST-запросы'
    })



def subscription_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        subscription = request.POST.get('subscription')
        

        SubscriptionRequest.objects.create(
            name=name,
            phone=phone,
            subscription=subscription
        )
        

        subject = 'Новая заявка на абонемент в BodyClub'
        message = f"""
        Поступила новая заявка на абонемент:
        
        Имя: {name}
        Телефон: {phone}
        Выбранный абонемент: {subscription}
        
        Дата заявки: {datetime.now().strftime('%d.%m.%Y %H:%M')}
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        try:

            payment = SubscriptionPayment(
                subscription_id=request.POST.get('subscription_id'),
                subscription_title=request.POST.get('subscription_title'),
                subscription_price=request.POST.get('subscription_price'),
                card_number=request.POST.get('card_number')[-4:],  
                card_name=request.POST.get('card_name'),
                email=request.POST.get('email'),
                payment_date=datetime.now()
            )
            payment.save()
            

            send_mail(
                'Оплата абонемента в BodyClub',
                f'''Благодарим вас за оплату абонемента!
                
                Детали оплаты:
                Абонемент: {payment.subscription_title}
                Сумма: {payment.subscription_price} ₽
                Дата: {payment.payment_date.strftime('%d.%m.%Y %H:%M')}
                
                Номер вашей карты: **** **** **** {payment.card_number}
                ''',
                settings.DEFAULT_FROM_EMAIL,
                [payment.email],
                fail_silently=False,
            )
            
            return JsonResponse({'success': True})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone']
            )
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'mainfitnes/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                redirect_url = request.session.pop('redirect_after_login', None) or 'profile'
                return redirect(redirect_url)
    else:

        if 'redirect' in request.GET:
            request.session['redirect_after_login'] = request.GET['redirect']
        form = LoginForm()
    return render(request, 'mainfitnes/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_view(request):
    return render(request, 'mainfitnes/profile.html')