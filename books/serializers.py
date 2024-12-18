from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title','author', 'year', 'genre', 'category', 'publisher', 'book_file', 'cover_image']

    def validate(self, data):
        print(data)
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

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'biography', 'birth_date', 'books']