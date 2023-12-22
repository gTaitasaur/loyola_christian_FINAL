from rest_framework import serializers
from seminario_app import models

class InscritoSerializer(serializers.ModelSerializer):
    institucion = serializers.StringRelatedField()
    class Meta:
        model = models.Inscrito
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institucion
        fields = '__all__'
