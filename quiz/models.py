from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    question_text = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    # explanation = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"Question {self.id}{self.question_text}"
    
    class Meta:
        ordering = ('id',)
    

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=250)

    def __str__(self):
        return self.choice_text
