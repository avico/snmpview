from django.db import models

class Alist(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    target = models.CharField(max_length=60, blank=True)
    problem = models.CharField(max_length=60, blank=True)
    trap = models.CharField(max_length=100, blank=True)
    varbinds = models.TextField(blank=True)
    ack = models.CharField(max_length=60, blank=True)

    class Meta:
        db_table = u'alist'
