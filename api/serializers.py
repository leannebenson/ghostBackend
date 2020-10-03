from rest_framework import serializers
from ghostPost.models import Boast_Roast

class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boast_Roast
        fields = ["id", "post_type", "content", "date_created", "total_votes"]
