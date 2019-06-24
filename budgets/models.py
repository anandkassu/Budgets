from django.db import models


class ExpenseAccount(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', blank=True, null=True)
    balance = models.IntegerField('Balance', default=0)

    def __str__(self):
        return self.title


class ExpenseCategory(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'ExpenseCategories'


class ExpenseItem(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', blank=True, null=True)
    account = models.ForeignKey(ExpenseAccount, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('Date', max_length=200)
    amount = models.IntegerField('Balance', default=0)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    title = models.CharField('Title', max_length=100)
    email = models.CharField('Email', max_length=20)
    message = models.TextField('Message', blank=True, null=True)

    def __str__(self):
        return self.title
