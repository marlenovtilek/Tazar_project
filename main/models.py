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
    avatar = models.ImageField("Фото участника")

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="places", null=True)
    name = models.CharField("Наименование", max_length=128)
    address = models.CharField("Адрес", max_length=256)
    phone = models.CharField("Контактный номер", max_length=128)
    working_from = models.CharField("Время открытия", max_length=10)
    working_to = models.CharField("Время закрытия", max_length=10)
    photo = models.ImageField("Картинка", upload_to="collection_places")
    material_type = models.ManyToManyField(MaterialType, related_name='collection_places')

    def __str__(self):
        return f'{self.name}'


class Partners(models.Model):
    avatar = models.ImageField(upload_to="partners_image")
    name = models.CharField("Наименование организации", max_length=128)
    address = models.CharField("Адрес организации", max_length=128)
    phone = models.CharField("Контакты организации", max_length=128, null=True)
    email = models.CharField("Электронная почта", max_length=50, null=True)
    description = models.TextField("Описание")
    urls = models.CharField("Ссылка на сайт", max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'

class Volunteers(models.Model):
    avatar = models.ImageField(upload_to="volunteers_photo")
    full_name = models.CharField("Имя волонтера", max_length=20)
    address = models.CharField("Адрес проживания", max_length=128)
    phone = models.CharField("Контактный номер", max_length=12)
    email = models.CharField("Электронная почта", max_length=50)
    education = models.TextField("Образование")

    class Meta:
        verbose_name = "Волонтер"
        verbose_name_plural = "Волонтеры"

    def __str__(self):
        return f'{self.full_name}'

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts' )
    image = models.ImageField("Фото точек приема пользователя", upload_to = "user_collection_places")
    name = models.CharField("Наименование организации", max_length=256)
    address = models.CharField("Адрес организации", max_length=256)
    phone = models.CharField("Контакты организации", max_length=128, null=True)
    working_from = models.CharField("Время открытия", max_length=10)
    working_to = models.CharField("Время закрытия", max_length=10)
    material_type = models.ManyToManyField(MaterialType, related_name='posts')

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return f'{self.name}'

