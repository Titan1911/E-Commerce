from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):

    def get(self, request):
        category = request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name=category)
        else:
            queryset = Product.objects.all()
        serializers = ProductSerializer(queryset, many=True)
        return Response({'data':serializers.data, 'count':len(serializers.data)})


@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        pass
    content = {'this is the first api': 'data contains all the products'}
    return Response(content, status=status.HTTP_200_OK)


