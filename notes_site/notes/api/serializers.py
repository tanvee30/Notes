from rest_framework.serializers import ModelSerializer


from notes.models import Notes


class NotesSerializer(ModelSerializer):
    class Meta:
        model=Notes
        fields='__all__'