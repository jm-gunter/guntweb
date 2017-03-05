from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Venue(models.Model):
    name = models.CharField(max_length=200)
    weburl = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateTimeField(null=True)
    imageurl = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200)
    rounds = models.ManyToManyField("Round", blank=True)
    teams = models.ManyToManyField("Team", blank=True)
    venue = models.ForeignKey(Venue, null=True)

    def add_new_team(self):
        self.teams.create(name = 'New Team')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Question(models.Model):
    category = models.ForeignKey(Category, default=0)
    text = models.TextField(null=True)
    image = models.ImageField(null=True, blank=True)
    answer = models.TextField(null=True)

    def __str__(self):
        return '{0}...'.format(self.text[:50])

class Round(models.Model):
    name = models.CharField(max_length=200)
    questions = models.ManyToManyField("Question", blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Score(models.Model):
    game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('game', 'round', 'team')
