from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    biography = models.TextField(blank=True, verbose_name='Биография')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    def __str__(self):
        return self.first_name

class Book(models.Model):
    GENRE_CHOICES = (
        ('M', 'Мистика'),
        ('R', 'Романтика'),
        ('H', 'Ужасы'),
        ('T', 'Триллер'),
        ('F', 'Фантастика'),
        ('P', 'Поэма'),

    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        help_text="Год выпуска должен быть от 1000 до 9999"
    )
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    book_file = models.FileField(upload_to='books/')

    class Meta:
        unique_together = ('title', 'author', 'year', 'publisher')

    def __str__(self):
        return f"{self.title} ({self.year})"