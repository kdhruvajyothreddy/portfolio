from django.db import models

# Create your models here.

# Create Blog Models
# title
# pub_date
# body
# image
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add the Blog app to the settings
# Create a migration
# Migrate
# Add to the admin

    def __str__(self): # To display list of blogs by 'title' on admin page
        return self.title

    def summary(self): # To limit number of characters to 100 for 'body'
        return self.body[:100]
    
    def pub_date_pretty(self): # To display date format limited to date only
        return self.pub_date.strftime('%b %e %Y')
