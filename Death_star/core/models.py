from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100, verbose_name='Зловещее название')

    def __str__(self):
        return self.name


class Recruit(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Родная планета')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почтовый ящик', max_length=254)

    def is_complete_test(self):
        if QuestionChoice.objects.filter(voted=self).distinct():
            return True
        else:
            return False

    def is_shadow_hand(self):
        siths = Sith.objects.all()
        for sith in siths:
            try:
                sith.padavans.get(id=self.id)
                return True
            except self.DoesNotExist:
                continue
        return False

    def __str__(self):
        return 'Новичок %s с %s' % (self.name, self.planet.name)


class Sith(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ужасающее имя')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Родная планета')
    padavans = models.ManyToManyField(Recruit, blank=True, verbose_name='Будущие ситхи')

    def __str__(self):
        return 'Владыка %s c %s' % (self.name, self.planet.name)


class ShadowHandQuestion(models.Model):
    description = models.TextField(max_length=254, verbose_name='Описание вопроса')

    def __str__(self):
        return self.description[0:50]


class QuestionChoice(models.Model):
    task = models.ForeignKey(ShadowHandQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250, verbose_name='Вариант ответа')
    voted = models.ForeignKey(Recruit, on_delete=models.CASCADE, verbose_name='Голосовавший', blank=True)

    def __str__(self):
        return 'Ответ на вопрос %d от %s' % (self.task.id, self.voted.name)
