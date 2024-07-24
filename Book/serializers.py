from rest_framework import serializers
from .models import Book, Genre, GenreBook

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GenreBookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = GenreBook
        fields = ['genre']

class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, write_only=True)
    book_genres = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genres', 'book_genres']

    def get_book_genres(self, obj):
        return GenreBookSerializer(obj.genrebook_set.all(), many=True).data

    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        book = Book.objects.create(**validated_data)
        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(**genre_data)
            GenreBook.objects.create(book=book, genre=genre)
        return book

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genres')
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.save()

        GenreBook.objects.filter(book=instance).delete()
        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(**genre_data)
            GenreBook.objects.create(book=instance, genre=genre)
        return instance
