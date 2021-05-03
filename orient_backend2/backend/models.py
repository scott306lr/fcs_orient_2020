from django.db import models

# Create your models here.

class Groupsinfo(models.Model):
    id = models.IntegerField(primary_key=True)


class Hint(models.Model):
    id = models.IntegerField(primary_key=True)
    hint_type = [(1, 'standard'), (2, 'interactive'), (3, 'photo'), (4, 'quiz')]
    hint_choices = models.CharField(choices=hint_type, max_length=40)
    difficulty = models.CharField(max_length = 100, default="null")
    name = models.CharField(max_length = 100)
    text = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    basic_score = models.IntegerField()
    bonus_score = models.IntegerField()
    penalty = models.IntegerField()
    where = models.CharField(max_length = 10, default ='')

class Hints(models.Model):
    # id = models.IntegerField(primary_key=True)
    hint_id = models.IntegerField(default=0)
    done_by = models.IntegerField(default=0)
    avail = models.CharField(max_length = 10, default ='')
    done = models.CharField(max_length = 10, default ='')
    whichgroup = models.ManyToManyField(Groupsinfo, related_name='hints')
    # whichgroup = models.ForeignKey(Groupsinfo, related_name='hints', on_delete=models.CASCADE)
    where = models.CharField(max_length = 10, default ='')

class Groups(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField()
    name = models.CharField(max_length = 100)

class Others(models.Model):
    id = models.IntegerField(primary_key=True)
    freeze = models.CharField(max_length = 10)
    cd_text = models.CharField(max_length = 1000, default='')

class Logging(models.Model):
    group_id = models.IntegerField()
    reason = models.CharField(max_length = 1000, default='')
    fin_time = models.CharField(max_length = 100)
    cur_score = models.IntegerField()
    get_score = models.IntegerField()



