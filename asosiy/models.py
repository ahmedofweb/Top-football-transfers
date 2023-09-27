from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=50)
    logo = models.FileField(null=True, blank=True)
    country = models.CharField(max_length=50)
    president = models.CharField(max_length=100, null=True, blank=True)
    coach = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    top_buy_tr = models.CharField(max_length=100, null=True, blank=True)
    top_sell_tr = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class  Player(models.Model):
    name = models.CharField(max_length=80)
    position = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    cost = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dob = models.DateField()
    def __str__(self):
        return self.name
class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    before_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='sold')
    after_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    cost = models.CharField(max_length=50)
    selling_cost = models.CharField(max_length=50)
    season = models.CharField(max_length=50, default='22-23')
    def __str__(self):
        return f"{self.player} from {self.before_club} to {self.after_club}"

class PresentSeason(models.Model):
    p_season = models.CharField(max_length=50)
