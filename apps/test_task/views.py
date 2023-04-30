from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ParaphraseSerializer


@api_view(['GET'])
def paraphrase_list(request):

    try:
        limit = int(request.GET.get('limit', ''))
    except ValueError:
        limit = 20

    data = {
        ParaphraseSerializer.syntax_tree_url_kwargs: request.GET.get(ParaphraseSerializer.syntax_tree_url_kwargs)
    }
    serializer = ParaphraseSerializer(data=data)
    if serializer.is_valid():
        paraphraser = serializer.validated_data[serializer.syntax_tree_url_kwargs]
        result_data = {
            'paraphrases': ParaphraseSerializer([phrase for i, phrase in zip(range(limit), paraphraser)], many=True).data
        }
        return Response(result_data)
    else:
        return Response({'errors': serializer.errors})
