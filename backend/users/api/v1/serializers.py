from rest_framework import serializers
from users.models import HGgfh


class HGgfhSerializer(serializers.ModelSerializer):
    class Meta:
        model = HGgfh
        fields = "__all__"
