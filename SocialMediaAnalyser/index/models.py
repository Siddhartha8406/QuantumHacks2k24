from django.db import models

class Doc(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    
    def __str__(self):
        return self.docfile.name
    
    