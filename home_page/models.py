from django.db import models

        # MOSH VIDEO 5.26.00 --> MAKEMIGRATION --> MIGRATE + STORE IN db.sqlite3
class Home(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Summary_om_oss(models.Model):
    titel = models.CharField(max_length=100)
    summary = models.CharField(max_length=5000)


class Snabbfakta(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)
    image = models.CharField(max_length=2083)
    head_quote = models.CharField(max_length=5000)
    last_updated = models.CharField(max_length=5000)
    quote = models.CharField(max_length=1000)
    quote_sayer = models.CharField(max_length=200)


class Intervju(models.Model):
    titel = models.CharField(max_length=100)
    front = models.CharField(max_length=400)
    image = models.CharField(max_length=2083)
    summary = models.CharField(max_length=600)
    par_one = models.CharField(max_length=2083)
    par_two = models.CharField(max_length=2083)
    par_three = models.CharField(max_length=2083)
    par_four = models.CharField(max_length=2083)
    par_five = models.CharField(max_length=2083)
    par_six = models.CharField(max_length=2083)
    par_seven = models.CharField(max_length=2083)
    par_eight = models.CharField(max_length=2083)
    par_nine = models.CharField(max_length=2083)
    par_ten = models.CharField(max_length=2083)
    auther = models.CharField(max_length=30)
    author_image = models.CharField(max_length=2083)


class Kontakt(models.Model):
    image = models.CharField(max_length=2083)
    mail = models.CharField(max_length=300)



