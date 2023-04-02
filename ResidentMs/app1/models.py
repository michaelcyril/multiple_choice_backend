from django.db import models


# Create your models here.

class JobVacancy(models.Model):
    company = models.CharField(max_length=30)
    jobTitle = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'job_vacancy'


class Requirement(models.Model):
    requirement = models.CharField(max_length=30)
    vacancy_id = models.ForeignKey(JobVacancy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.requirement} at {self.vacancy_id.jobTitle}'

    class Meta:
        db_table = 'requirement'


class Question(models.Model):
    question = models.TextField()
    vacancy_id = models.ForeignKey(JobVacancy, on_delete=models.CASCADE, null=True)
    is_checkable = models.BooleanField(default=False)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'answer'

    def __str__(self):
        return f'question {self.question_id.question} answer {self.answer}'

