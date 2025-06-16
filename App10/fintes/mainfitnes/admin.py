from django.contrib import admin
from .models import Subscription
from .models import PersonalTraining
from .models import GroupWorkout
from .models import Review
from .models import TrainingSignUp
from .models import CallbackRequest
from .models import SubscriptionRequest
from .models import SubscriptionPayment

@admin.register(SubscriptionPayment)
class SubscriptionPaymentAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'subscription_title', 'subscription_price', 'payment_date')
    list_filter = ('payment_date',)
    search_fields = ('card_name', 'email', 'subscription_title')
    readonly_fields = ('payment_date',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'branch', 'price', 'is_active')
    list_filter = ('branch', 'is_active')
    search_fields = ('title', 'features')

@admin.register(PersonalTraining)
class PersonalTrainingAdmin(admin.ModelAdmin):
    list_display = ('sessions', 'trainer_type', 'price', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('trainer_type', 'is_active')
    search_fields = ('description',)

@admin.register(GroupWorkout)
class GroupWorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'branch', 'trainer', 'time', 'is_active')
    list_filter = ('branch', 'is_active')
    search_fields = ('title', 'trainer', 'description')
    list_editable = ('is_active',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'content')
    list_filter = ('created_at',)
    search_fields = ('name', 'content')

@admin.register(TrainingSignUp)
class TrainingSignUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'training_type', 'training_id', 'created_at')
    list_filter = ('training_type', 'created_at')
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('created_at',)


@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    search_fields = ('name', 'phone')
    list_filter = ('created_at',)


@admin.register(SubscriptionRequest)
class SubscriptionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subscription', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'subscription')