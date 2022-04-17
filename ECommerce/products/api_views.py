from rest_framework.views import APIView
from rest_framework.response import Response
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


