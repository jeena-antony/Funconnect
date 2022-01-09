from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class game(models.Model):
    def __str__(self) -> str:
        return self.game_name

    game_name=models.CharField(max_length=100)
    game_desc=models.CharField(max_length=200)
    game_img=models.CharField(max_length=500,default="https://www.food4fuel.com/wp-content/uploads/woocommerce-placeholder-600x600.png")

class question(models.Model):
    def __str__(self) -> str:
        return self.question
    
    game_id =models.ForeignKey(game,on_delete=models.CASCADE,default=1)
    question=models.CharField(max_length=200)
    answer=models.IntegerField()
    # options=models.CharField(max_length=500)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)

class mark(models.Model):
    # def __str__(self) -> str:
    #     return self.mark
    
    user_id =models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    game_id =models.ForeignKey(game,on_delete=models.CASCADE,default=1)
    mark=models.IntegerField()