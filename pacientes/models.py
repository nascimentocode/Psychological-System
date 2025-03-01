from django.db import models
from django.urls import reverse

class Pacientes(models.Model):
    reason_choices = (
        ('TDAH', 'Transtorno de déficit de atenção com hiperatividade'),
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
        ('TAG', 'Transtorno de ansiedade generalizada')
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='photos')
    payment_up_to_date = models.BooleanField(default=True)
    reason_for_visit = models.CharField(max_length=4, choices=reason_choices)

    def __str__(self):
        return self.name


class Tarefas(models.Model):
    frequencia_choices = (
        ('D', 'Diário'),
        ('1S', '1 vez por semana'),
        ('2S', '2 vezes por semana'),
        ('3S', '3 vezes por semana'),
        ('N', 'Ao necessitar')
    )
    tarefa = models.CharField(max_length=255)
    instrucoes = models.TextField()
    frequencia = models.CharField(max_length=2, choices=frequencia_choices, default='D')

    def __str__(self):
        return self.tarefa


class Consultas(models.Model):
    humor = models.PositiveIntegerField()
    registro_geral = models.TextField()
    video = models.FileField(upload_to="video")
    tarefas = models.ManyToManyField(Tarefas)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paciente.name
    
    @property
    def link_publico(self):
        return f"http://127.0.0.1:8000{reverse('consulta_publica', kwargs={'id': self.id})}"
    
    @property
    def views(self):
        views = Visualizacoes.objects.filter(consulta=self)
        totais = views.count()
        unicas = views.values('ip').distinct().count()
        return f'{totais} - {unicas}'

class Visualizacoes(models.Model):
    consulta = models.ForeignKey(Consultas, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()