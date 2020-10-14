from django.db import models
from apps.acceso.models import User

# Create your models here.


#modelo entrenamientos
class Training(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    descript = models.CharField(max_length=255, null=True, blank=True)
    repetition = models.PositiveIntegerField()  
    duration = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.descript)


    class Meta:
        verbose_name = 'Entrenamiento'
        verbose_name_plural = 'Entrenamientos'

#modelo deporte
class Sport(models.Model):    
    name = models.CharField(max_length = 50)
    descript = models.CharField(max_length = 255, null=True, blank=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Deporte'
        verbose_name_plural = 'Deportes'


#modelo entrenador
class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, deporte:{}".format(self.user,self.sport)

    class Meta:
        verbose_name = 'Entrenador'
        verbose_name_plural = 'Entrenadores'

#modelo atleta
class Athlete(models.Model):
    user = models.OneToOneField(User, related_name = 'user', on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    hit = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weigth = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    muscle = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {} {}".format(self.user,self.hit,self.weigth,self.muscle)

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'




