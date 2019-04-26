from django.forms import ModelForm
from directory.models import CreateAuthor



class CreateForm(ModelForm):
    model = CreateAuthor
