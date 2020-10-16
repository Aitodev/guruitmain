from django.db import models


class Applications(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    mail = models.CharField(verbose_name='Почта', max_length=200)
    comment = models.CharField(verbose_name='Коммент', max_length=200)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, null=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Заявка cо страницы контактов'
        verbose_name_plural = 'Заявка со страницы контактов'


class Team(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    img = models.ImageField(verbose_name='Фото участника команды', upload_to='static/images/team/', null=True,)
    status = models.CharField(verbose_name='Статус', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', max_length=200, blank=True)
    instagram = models.CharField(verbose_name='Ссылки на instagram', max_length=200, blank=True)
    mail = models.CharField(verbose_name='Почта участника', max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'


class Services(models.Model):
    img = models.ImageField(verbose_name='Фото услуги', upload_to='static/images/team/', null=True,)
    namemain =  models.CharField(verbose_name='Заголовок', max_length=200)
    description = models.CharField(verbose_name='Описание', max_length=200)
    price = models.CharField(verbose_name='Цена', max_length=200)

    def __str__(self):
        return self.namemain

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

