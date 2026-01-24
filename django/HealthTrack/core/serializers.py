from rest_framework import serializers
from django.contrib.auth.models import User
import requests
from .models import Paciente

class CadastroPacienteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    cep = serializers.CharField(max_length=9)

    class Meta:
        model = Paciente
        fields = ['username', 'password', 'cep', 'endereco']

    def validate_cep(self, value):
        cep_limpo = value.replace('-', '')
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        response = requests.get(url)

        if response.status_code != 200 or "erro" in response.json():
            raise serializers.ValidationError("CEP inválido")

        self.context['endereco_api'] = response.json().get('Logradouro', 'N/A')
        return value

    def create(self, validation_data):

        user_data = {
            'username': validated_data('username'),
            'password': validated_data('password')
        }

        user = User.objects.create_user(**user_data)

        from django.contrib.auth.models import Group
        group = Group.objects.get(name='Paciente')
        user.groups.add(group)

        validated_data['endereco'] = self.contexto['endereco_api']
        paciente = Paciente.objects.create(user=user, **validated_data)

        return paciente