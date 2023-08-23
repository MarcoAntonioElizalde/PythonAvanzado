from django.contrib import admin
from .models import User, Account, Card, Charge, Payment

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Charge)
admin.site.register(Payment)