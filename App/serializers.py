from .models import Book
from rest_framework import serializers

## Using Function based serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre',  'date', 'release_date']



## Class based serializer
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     author = serializers.CharField(max_length=50)
#     genre = serializers.CharField(max_length=50)
#     date = serializers.DateTimeField()
#     release_date = serializers.DateField()
#
#     def create(self, validate_data):
#         return Book.objects.create(validate_data)
#
#     def update(self, instance, validate_data):
#         instance.title = validate_data.get('title', instance.title)
#         instance.author = validate_data.get('author', instance.author)
#         instance.genre = validate_data.get('genre', instance.genre)
#         instance.date = validate_data.get('date', instance.date)
#         instance.release_date = validate_data.get('release_date', instance.release_date)
#         instance.save()
#         return instance
