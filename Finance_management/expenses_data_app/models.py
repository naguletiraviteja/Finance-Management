from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class CreateExpense(models.Model):
    expense_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    date_of_expense = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.category}"