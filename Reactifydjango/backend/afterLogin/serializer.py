from rest_framework import serializers

from accounts.models import Clearance


class InfoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clearance
        fields = ['student', 'Department', 'Clear',
                  'DateCleared', 'name']
