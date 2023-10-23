from oscar.core.loading import get_model
from rest_framework import generics

from ka_be_offer.apps.offerv2.serializers import OfferSerializer

Offer = get_model('offer', 'Benefit')


# Create your views here.
class OfferList(generics.ListAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class OfferDetail(generics.RetrieveAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
