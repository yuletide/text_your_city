from django.db import models
import datetime

POLL_TYPE_CHOICES = (
    ('open', 'Open answer'),
    ('multi', 'Multiple choice'),
)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    edit_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    open_date = models.DateTimeField('start date of poll')
    close_date = models.DateTimeField('end date of poll')
    poll_number = models.CharField(max_length=15)
    
    poll_type = models.CharField(max_length=20, choices=POLL_TYPE_CHOICES)
    
    def __unicode__(self):
	return self.question 

    def is_open(self):
        if open_date <= datetime.date.now() <= close_date:
            return True
        else:
            return False

    #def was_published_today(self):
    #    return self.pub_date.date() == datetime.date.today()
    #was_published_today.short_description = 'Published today?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
	return self.choice

class Response(models.Model):
    poll = models.ForeignKey(Poll)
    raw = models.CharField(max_length=200)
    from_number = models.CharField(max_length=50)
    to_number = models.CharField(max_length=50)
    
    def clean(self):
        if not poll.is_open():
            raise ValidationError('Poll is not currently running')
        # check that 
