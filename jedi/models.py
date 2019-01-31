from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=30)
    homeplanet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Test(models.Model):
    order_code = models.IntegerField()
    question1 = models.CharField(max_length=50, default=1)
    answer1 = models.IntegerField(choices=((1, "Yes"), (2, "Nope")), default=1)
    question2 = models.CharField(max_length=50, default=2)
    answer2 = models.IntegerField(choices=((1, "Yes"), (2, "Nope")), default=1)
    question3 = models.CharField(max_length=50, default=3)
    answer3 = models.IntegerField(choices=((1, "Yes"), (2, "Nope")), default=1)

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='test', null=True)


class Jedi(models.Model):
    name = models.CharField(max_length=30)
    edu_planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
