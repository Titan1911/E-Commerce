from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductImage, Category
from .serializers import ProductSerializer, ProductImageSerializer, CategorySerializer

# class ProductView(APIView):

#     def get(self, request):
#         # print(request.query_params)
#         category = request.query_params.get('category')
#         if category:
#             queryset = Product.objects.filter(category__category_name=category)
#             print(queryset)
#         else:
#             queryset = Product.objects.all()
#         serializers = ProductSerializer(queryset, many=True)
#         return Response({'data':serializers.data, 'count':len(serializers.data)})

#     def post(self, request):
#         pass

#     def put(self, request):
#         pass


@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        slug = request.query_params.get('category')
        quantity = request.query_params.get('quantity')
        size = request.query_params.get('size')
        color = request.query_params.get('color')
        if slug:
            products = Product.objects.filter(category__slug=slug)
        if quantity:
            products = products.filter(quantity_type__variant_name=quantity)
        if size:
            products = products.filter(size_type__size_name=size)
        if color:
            products = products.filter(color_type__color_name=color)
        if not (color or quantity or slug):
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        print(serializer)
        data = {'count': len(serializer.data), 'products': serializer.data}
        return Response(data=data, status=200)

    else:
        error_msg = {'error': f'Method {request.method} not allowed.'}
        return Response(data=error_msg, status=405)


@api_view(['GET','POST','PUT'])
def product(request, id):
    try:
        product = Product.objects.get(id=id)
        # print(product.image)
        images = ProductImage.objects.filter(product=product)

    except Product.DoesNotExist:
        error_msg = {'error' : f"Product with id={id} doesn't exists"}
        return Response(data=error_msg, status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        image_serializer = ProductImageSerializer(images, many=True)
        data = {'count': 1, 'product': serializer.data}
        # This line of code was needed when related_name wasn't used in ProductImage
        # data['product']['images'] = image_serializer.data 
        # This is line of code is manually searching for product and get its images
        return Response(data=data, status=200)

    elif request.method == 'PUT':
        data = request.data
        serializer = ProductSerializer(product, data=data)
        # print(data)
        # product_serializer = ProductImageSerializer(images, data=data, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
        
        data = {'count': 1, 'product': serializer.data}
        return Response(data=data, status=201)

    elif request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)

        data = {'count': 1, 'product': serializer.data} 
        return Response(data=data, status=201)
        


@api_view(['GET'])
def categories(request):
    if request.method=='GET':
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        data = {'count': len(categories_serializer.data), 'categories':categories_serializer.data}
        return Response(data=data, status=200)

