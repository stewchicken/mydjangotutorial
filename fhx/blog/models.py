from django.db import models

class Article(models.Model):
    title=models.CharField("title",max_length=50)
    author=models.CharField("author",max_length=50)
    created_date=models.DateField("created date", auto_now_add=True)
    modify_date=models.DateField("modify date", auto_now_add=True)
    content=models.TextField()
    is_shown=models.BooleanField() 

    class Meta:
        db_table="article"
    def _str_(self):
        return self.title

