from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    branch = models.CharField('Филиал', max_length=100, choices=[
        ('dvor', 'Дворцовая 4А'),
        ('repina', 'ул. Репина 4'),
        ('lenina', 'пр. Ленинского Комсомола 34')
    ])
    title = models.CharField('Название', max_length=200)
    price = models.IntegerField('Цена')
    duration = models.CharField('Срок действия', max_length=50)
    features = models.TextField('Особенности')
    is_active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return f"{self.title} ({self.get_branch_display()})"


class PersonalTraining(models.Model):
    TRAINER_TYPE = [
        ('regular', 'Персональный тренер'),
        ('master', 'Мастер-тренер'),
    ]
    
    sessions = models.PositiveIntegerField('Количество тренировок')
    trainer_type = models.CharField('Тип тренера', max_length=20, choices=TRAINER_TYPE)
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание', blank=True)
    is_active = models.BooleanField('Активно', default=True)

    def __str__(self):
        return f"{self.sessions} тренировок ({self.get_trainer_type_display()})"
    

class GroupWorkout(models.Model):
    BRANCH_CHOICES = [
        ('dvor', 'Дворцовая 4А'),
        ('repina', 'ул. Репина 4'),
        ('lenina', 'пр. Ленинского Комсомола 34')
    ]
    
    title = models.CharField('Название тренировки', max_length=200)
    branch = models.CharField('Филиал', max_length=20, choices=BRANCH_CHOICES)
    trainer = models.CharField('Тренер', max_length=100)
    description = models.TextField('Описание')
    time = models.CharField('Время', max_length=50)
    days = models.CharField('Дни недели', max_length=100)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.get_branch_display()})"
    

class Review(models.Model):
    name = models.CharField('Имя', max_length=100)  
    content = models.TextField('Отзыв')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)  

    def __str__(self):
        return f"Отзыв от {self.name} ({self.created_at})"
    

class TrainingSignUp(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', blank=True)
    training_type = models.CharField('Тип тренировки', max_length=20) 
    training_id = models.IntegerField('ID тренировки')
    created_at = models.DateTimeField('Дата записи', auto_now_add=True)

    def __str__(self):
        return f"Запись от {self.name} на тренировку {self.training_id}"


class CallbackRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"
    
class SubscriptionRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    subscription = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subscription}"
    
class SubscriptionPayment(models.Model):
    subscription_id = models.CharField(max_length=100)
    subscription_title = models.CharField(max_length=255)
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=4)
    card_name = models.CharField(max_length=255)
    email = models.EmailField()
    payment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.card_name} - {self.subscription_title} ({self.payment_date})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    address = models.CharField('Адрес', max_length=255, blank=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True)
    
    def __str__(self):
        return self.user.username
    
