from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.TextField(null=False)
    first_name = models.TextField(null=True)
    birthdate = models.TextField(null=False)
    password = models.TextField(null=False)
        
    def authenticate(email, password):
        return Users.objects.filter(email=email, password=password).exists()
         
    def mails_sent(self):
        return Mails.objects.filter(source=self.email)
    
    def mails_received(self):
        return Mails.objects.filter(destination=self.email)
    
    def mails_spam(self):
        return Mails.objects.filter(destination=self.email, is_spam=1)
        
class Mails(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sent_mails')
    destination = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='received_mails')
    mail_object = models.TextField()
    content = models.TextField()
    action_date = models.DateTimeField()
    state = models.IntegerField(choices=[(0, 'Not Read'), (1, 'Read'), (2, 'Deleted')])
    is_spam = models.IntegerField(choices=[(0, 'Not Spam'), (1, 'Spam')])
    