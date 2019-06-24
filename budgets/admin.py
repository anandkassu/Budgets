from django.contrib import admin
from .models import ExpenseAccount
from .models import ExpenseItem
from .models import ExpenseCategory
from .models import Message


admin.site.register(ExpenseAccount)

admin.site.register(ExpenseItem)

admin.site.register(ExpenseCategory)

admin.site.register(Message)

