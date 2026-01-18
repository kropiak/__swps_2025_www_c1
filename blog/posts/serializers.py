from rest_framework import serializers
from .models import Topic, Category, Post


class TopicSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created = serializers.DateTimeField(required=False, read_only=True)

    # przesłonięcie metody create() z klasy serializers.Serializer
    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    # wykorzystywana przy żądaniach aktualizacji obiektu przez REST API
    # np. żądaniu typu PUT oraz PATCH
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    # Ctrl + / - dodanie/usunięcie komentarza dla zaznaczonych linii

    def validate_name(self, value):
        temp_value = value.strip().replace(' ','')
        if not temp_value.isalpha():
            raise serializers.ValidationError(
                "Nazwa musi zawierać tylko litery!",
            )
        return value


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        # musimy wskazać klasę modelu
        model = Category
        # definiując poniższe pole możemy określić listę właściwości modelu,
        # które chcemy serializować
        fields = ['id', 'name', 'description']
        # definicja pola modelu tylko do odczytu
        read_only_fields = ['id']


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        # musimy wskazać klasę modelu
        model = Post
        # definiując poniższe pole możemy określić listę właściwości modelu,
        # które chcemy serializować
        fields = ['id', 'title', 'text', 'topic', 'slug', 'created_at', 'updated_at', 'created_by']
        # definicja pola modelu tylko do odczytu
        read_only_fields = ['id', 'created_at', 'updated_at']