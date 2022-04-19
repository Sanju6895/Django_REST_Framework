import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

"""
Serializers allow complex data such as querysets and model instances to
be converted to native Python datatypes that can then 
be easily rendered into JSON , XML or other content types
"""

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    data = {}
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)

    return Response(serializer.data)