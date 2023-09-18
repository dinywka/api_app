from rest_framework import serializers
from .models import News, Complaint

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('name', 'title', 'news')

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('name', 'description')