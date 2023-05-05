from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        "Пользователь",
        max_length=150,
        unique=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True, # для базы
        blank=True, # для формы 
        verbose_name="Фото профиля"
    )
    phone = models.CharField("Номер телефона", max_length=14, null=True)
    email = models.EmailField("Почта", blank=True, null=True)
    address = models.CharField("Адрес прожвания", max_length=256, null=True)


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.username)


class AboutUs(models.Model):
    title = models.CharField("Название", max_length=100)


class Members(models.Model):
    full_name = models.CharField("Полное имя", max_length=50)
    age = models.CharField("Возраст", max_length=10)
    position = models.CharField("Должность", max_length=50)
    description = models.TextField("Описание")
    avatar = models.ImageField(upload_to="Фото участника")

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return self.description[:50]


class MaterialType(models.Model):
    name = models.CharField("Название сырья", max_length=128)
    is_active = models.BooleanField("Актуально", default=True)

    def __str__(self):
        return f'{self.name}'

class CollectionPlaces(models.Model):
    name = models.CharField("Наименование пункта", max_length=128)
    address = models.CharField("Адрес пункта", max_length=256)
    phone = models.CharField("Контактный номер", max_length=128)
    working_hours = models.CharField("График работы", max_length=100)
    photo = models.ImageField("Картинка", upload_to="collection_places")
    email = models.CharField("Электронная почта", max_length=50)
    material_type = models.ManyToManyField(MaterialType)

    def __str__(self):
        return f'{self.name}'


class Partners(models.Model):
    avatar = models.ImageField(upload_to="partners_image")
    name = models.CharField("Наименование организации", max_length=128)
    address = models.CharField("Адрес организации", max_length=128)
    phone = models.CharField("Контакты организации", max_length=128, null=True)
    email = models.CharField("Электронная почта", max_length=50, null=True)
    description = models.TextField("Описание", null=True)
    urls = models.CharField("Ссылка на сайт", max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'

class Volunteers(models.Model):
    avatar = models.ImageField(upload_to="volunteers_photo")
    first_name = models.CharField("Имя волонтера", max_length=20, null=True)
    last_name = models.CharField("Фамилия волонтера", max_length=20, null=True)
    address = models.CharField("Адрес проживания", max_length=128)
    phone = models.CharField("Контактный номер", max_length=12)
    email = models.CharField("Электронная почта", max_length=50)
    education = models.TextField("Образование")
    age = models.PositiveIntegerField("Возраст", null=True)

    class Meta:
        verbose_name = "Волонтер"
        verbose_name_plural = "Волонтеры"

    def __str__(self):
        return f'{self.full_name}'

