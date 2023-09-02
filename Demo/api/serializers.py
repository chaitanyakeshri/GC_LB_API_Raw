from rest_framework import serializers
from articles.models import Article, GCs , Score_Board, Hostel

#serializer are required to channel the data
#  in JSON format so that it can be sent over network

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class GCsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCs 
        fields = '__all__'

class GCsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GCs
        fields = ['GC_Name']

class Score_BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score_Board 
        fields = '__all__'

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'
