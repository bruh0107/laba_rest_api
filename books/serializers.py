from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['category'] == 'T':
            if Book.objects.filter(
                title=data['title'],
                year=data['year'],
                publisher=data['publisher']
            ).exists():
                raise serializers.ValidationError('Учебник с таким названием, годом и издателем уже существует.')

        elif data['category'] == 'F':
            if Book.objects.filter(
                title=data['title'],
                author=data['author'],
                year=data['year'],
                publisher=data['publisher']
            ).exists():
                raise serializers.ValidationError("Эта художественная книга уже добавлена.")

        return data