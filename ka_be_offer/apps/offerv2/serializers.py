from oscar.core.loading import get_model
from oscarapi.serializers.utils import (
    OscarModelSerializer
)


Offer = get_model('offer', 'Benefit')


class OfferSerializer(OscarModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
