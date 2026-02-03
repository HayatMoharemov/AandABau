from django.db import models

from common.validators import name_validator


class CreateFeedback(models.Model):

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ['-created_at']

    class Rating(models.IntegerChoices):
        VERY_BAD = 1, 'Very bad'
        BAD = 2, 'Bad'
        AVERAGE = 3, 'Average'
        GOOD = 4, 'Good'
        EXCELLENT = 5, 'Excellent'

    name = models.CharField(
        validators=[name_validator]
    )
    rating = models.IntegerField(
        choices = Rating.choices
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.rating} - {self.get_rating_display()}"