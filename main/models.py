from django.db import models


class Task(models.Model):
    title = models.CharField('Task Name', max_length=50)
    description = models.TextField('Describe text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

