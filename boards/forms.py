from django import forms
from .models import Board

class BoardCreationForm(forms.ModelForm):
  class Meta:
    model = Board
    fields = ["title", "content" ]

    def save(self, **kwargs):
        board = super().save(commit=False)
        return board