from django.forms import ModelForm
from app.models import Pessoas, Unidades

# Create the form class.
class PessoasForm(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['nome', 'sexo', 'idade', 'telefone', 'email']


class UnidadesForm(ModelForm):
    class Meta:
        model = Unidades
        fields = ['nindentifica', 'proprietario', 'condominio', 'endereco']
