from django.db import models
# Create your models here.

# add this
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title


# add this
class User(models.Model):
  userName = models.CharField(max_length=120)
  password = models.TextField()

  def _str_(self):
    return self.userName

