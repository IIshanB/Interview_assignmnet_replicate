from rest_framework import serializers

class GenerateImageSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=255)
    width = serializers.IntegerField(default=512)
    height = serializers.IntegerField(default=512)
