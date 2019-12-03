from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_text = RichTextField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    answer_title = models.CharField(max_length=200)
    answer_text = RichTextField()
    pub_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_title