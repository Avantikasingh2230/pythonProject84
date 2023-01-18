from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import VendorRegisterSerializer, CustomerRegisterSerializer, ChangePasswordSerializer, \
    vendorInfoSerializer, vendortypeSerializer, Aboutpageserializer, carmicropageserializer, addpicturesSerializer, \
    venueSerializer, cateringSerializer, vanuecateringSerializer, dropimageSerializer, djSerializer, dholSerializer, portpolioSerializer, engagementSerializer, preweddingSerializer, weddingSerializer, allweddingSerializer,engagementmakeupSerializer, preweddingmakeupSerializer, weddingmakeupSerializer, allweddingmakeupSerializer,foodplateSerializer, foodwithoutSerializer,foodwithSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


# Create your views here.
class RegisterView(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: VendorRegisterSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = VendorRegisterSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: VendorRegisterSerializer(many=True)}, request_body=VendorRegisterSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = VendorRegisterSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: VendorRegisterSerializer(many=True)}, request_body=VendorRegisterSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = VendorRegisterSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )


# customer registration
class CustomerRegisterView(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: CustomerRegisterSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = CustomerRegisterSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: CustomerRegisterSerializer(many=True)},
                         request_body=CustomerRegisterSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = CustomerRegisterSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: CustomerRegisterSerializer(many=True)}, request_body=CustomerRegisterSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = CustomerRegisterSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )


# logout and logoutall
class LogOutAPIView(APIView):
    def post(self, request, format=None):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# change password

# class RegisterAPIView(APIView):
#     serializer_class = VendorRegisterSerializer
#
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#
#             refresh = RefreshToken.for_user(user)
#
#             response_data =  {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user': serializer.data,
#             }
#
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#
#             refresh = RefreshToken.for_user(user)
#
#             response_data =  {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user': serializer.data,
#             }
#
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def put(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#
#             refresh = RefreshToken.for_user(user)
#
#             response_data =  {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user': serializer.data,
#             }
#
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# customer registration
# class CustomerRegisterAPIView(APIView):
#     serializer_class = CustomerRegisterSerializer
#
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#
#             refresh = RefreshToken.for_user(user)
#
#             response_data =  {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user': serializer.data,
#             }
#
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#
#             refresh = RefreshToken.for_user(user)
#
#             response_data =  {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user': serializer.data,
#             }
#
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def put(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#
#             refresh = RefreshToken.for_user(user)
#
#             response_data =  {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user': serializer.data,
#             }
#
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    # permission_classes = (IsAuthenticated,)
    AUTHENTICATION_CLASSES = [JWTAuthentication]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            # if not self.object.check_password(serializer.data.get("old_password")):
            #     return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# vendor type serializer
class vendortypeView(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: vendortypeSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = vendortypeSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: vendortypeSerializer(many=True)}, request_body=vendortypeSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = vendortypeSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: VendorRegisterSerializer(many=True)}, request_body=VendorRegisterSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = VendorRegisterSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )


class vendorinfoView(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: vendorInfoSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = vendorInfoSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: vendorInfoSerializer(many=True)}, request_body=vendorInfoSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = vendorInfoSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: vendorInfoSerializer(many=True)}, request_body=vendorInfoSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = VendorRegisterSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )


# vendor about us page
class vendoraboutView(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: Aboutpageserializer(many=True)}, request_body=Aboutpageserializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = Aboutpageserializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: Aboutpageserializer(many=True)}, request_body=Aboutpageserializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = Aboutpageserializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
    # images homepage


# class ImageView(APIView):
#         parser_classes = [MultiPartParser, ]
#
#         # permission_classes = [IsAuthenticated]
#
#
#
#
#         def post(self, request, *args, **kwargs):
#             data = request.data
#             serializers = imageserializer(data=data)
#             serializers.is_valid(raise_exception=True)
#             serializers.save()
#             return Response(
#                 {"desc": serializers.data},
#                 status=status.HTTP_200_OK
#             )

# @swagger_auto_schema(
#     manual_parameters=[
#         openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id",
#                           type=openapi.TYPE_STRING),
#     ],
#     responses={200: imageserializer(many=True)}, request_body=imageserializer
# )
# def put(self, request, *args, **kwargs):
#     User_Group_id = request.query_params.get('User_Group_id', None)
#     User_Group = get_object_or_404(Ticket, pk=User_Group_id)
#
#     serializer = imageserializer(ticket, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     print(request.data)
#     serializer.save()
#     return Response(
#         {"desc": serializers.data},
#         status=status.HTTP_200_OK
#     )

# car api
class CarView(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: carmicropageserializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = carmicropageserializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: carmicropageserializer(many=True)}, request_body=carmicropageserializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = carmicropageserializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: carmicropageserializer(many=True)}, request_body=VendorRegisterSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = carmicropageserializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )


# img field
# class ImageView(APIView):
#     parser_classes = [MultiPartParser,]
#     # permission_classes = [IsAuthenticated]
#
#     @swagger_auto_schema(responses={200: imageserializer(many=True)})
#     def get(self, request, *args, **kwargs):
#         qs = User.objects.all()
#         serializers = imageserializer(qs, many=True)
#         return Response(
#             serializers.data,
#             status=status.HTTP_200_OK
#         )
#
#     @swagger_auto_schema(responses={200: imageserializer(many=True)}, request_body=imageserializer)
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializers = imageserializer(data = data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(
#             {"desc": serializers.data},
#             status = status.HTTP_200_OK
#         )
#
#
#
#     @swagger_auto_schema(
#     manual_parameters=[
#         openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
#     ],
#     responses={200: imageserializer(many=True)}, request_body=imageserializer
#     )
#     def put(self, request, *args, **kwargs):
#         User_Group_id = request.query_params.get('User_Group_id', None)
#         User_Group = get_object_or_404(Ticket, pk=User_Group_id)
#
#         serializer = imageserializer(ticket, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         print(request.data)
#         serializer.save()
#         return Response(
#             {"desc": serializers.data},
#             status = status.HTTP_200_OK
# add pictures
# )
class addpic(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: addpicturesSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = addpicturesSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: addpicturesSerializer(many=True)}, request_body=addpicturesSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = addpicturesSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: addpicturesSerializer(many=True)}, request_body=addpicturesSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = addpicturesSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )


# venue services
class venueservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: venueSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = venueSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: venueSerializer(many=True)}, request_body=venueSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = venueSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: venueSerializer(many=True)}, request_body=venueSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = venueSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#catering services
class cateringservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: cateringSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = cateringSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: cateringSerializer(many=True)}, request_body=cateringSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = cateringSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: cateringSerializer(many=True)}, request_body=cateringSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = cateringSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#combined catering and venue services
class venuecateringservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: vanuecateringSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = vanuecateringSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: vanuecateringSerializer(many=True)}, request_body=vanuecateringSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = vanuecateringSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: vanuecateringSerializer(many=True)}, request_body=vanuecateringSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = vanuecateringSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#drop image view
class dropimage(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: dropimageSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = dropimageSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:dropimageSerializer(many=True)}, request_body=dropimageSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = dropimageSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: dropimageSerializer(many=True)}, request_body=dropimageSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = dropimageSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#music services
class djservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: djSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = djSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:djSerializer(many=True)}, request_body=djSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = djSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: djSerializer(many=True)}, request_body=djSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = djSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
class dholservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: djSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = dholSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:dholSerializer(many=True)}, request_body=dholSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = dholSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: dholSerializer(many=True)}, request_body=dholSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = dholSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#camera services
#portpolio
class portpolioservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: portpolioSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = portpolioSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:portpolioSerializer(many=True)}, request_body=portpolioSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = portpolioSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: portpolioSerializer(many=True)}, request_body=dholSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = portpolioSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#engegement serializers
class engegementservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: engagementSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = engagementSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:engagementSerializer(many=True)}, request_body=engagementSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = engagementSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: engagementSerializer(many=True)}, request_body=engagementSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = engagementSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#only preweddding
class preweddingservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: preweddingSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = preweddingSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:preweddingSerializer(many=True)}, request_body=preweddingSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = preweddingSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: preweddingSerializer(many=True)}, request_body=preweddingSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = preweddingSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#only wedding
class weddingservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: weddingSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = weddingSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:weddingSerializer(many=True)}, request_body=weddingSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = weddingSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: weddingSerializer(many=True)}, request_body=weddingSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = weddingSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#all 3 wedding
class allweddingservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: allweddingSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = allweddingSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:allweddingSerializer(many=True)}, request_body=allweddingSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = allweddingSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: allweddingSerializer(many=True)}, request_body=allweddingSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = allweddingSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#makeup services
#engegement serializers
class engegementmakeupservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: engagementmakeupSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = engagementmakeupSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:engagementmakeupSerializer(many=True)}, request_body=engagementmakeupSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = engagementmakeupSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: engagementmakeupSerializer(many=True)}, request_body=engagementmakeupSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = engagementmakeupSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#only preweddding
class preweddingmakeupservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: preweddingmakeupSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = preweddingmakeupSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:preweddingmakeupSerializer(many=True)}, request_body=preweddingmakeupSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = preweddingmakeupSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: preweddingmakeupSerializer(many=True)}, request_body=preweddingmakeupSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = preweddingmakeupSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#only wedding
class weddingmakeupservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: weddingmakeupSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = weddingmakeupSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:weddingmakeupSerializer(many=True)}, request_body=weddingmakeupSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = weddingmakeupSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: weddingmakeupSerializer(many=True)}, request_body=weddingmakeupSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = weddingmakeupSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#all 3 wedding
class allweddingmakeupservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: allweddingmakeupSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = allweddingmakeupSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:allweddingmakeupSerializer(many=True)}, request_body=allweddingmakeupSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = allweddingmakeupSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: allweddingmakeupSerializer(many=True)}, request_body=allweddingmakeupSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = allweddingmakeupSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#food services
class foodplateservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: foodplateSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = foodplateSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:foodplateSerializer(many=True)}, request_body=foodplateSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = foodplateSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: foodplateSerializer(many=True)}, request_body=foodplateSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = foodplateSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#food with material
class foodwithoutservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: foodwithoutSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = foodwithoutSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:foodwithoutSerializer(many=True)}, request_body=foodwithoutSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = foodwithoutSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: foodwithoutSerializer(many=True)}, request_body=foodwithoutSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = foodwithoutSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#food with material
class foodwithservices(APIView):
    parser_classes = [MultiPartParser, ]

    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: foodwithSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializers = foodwithSerializer(qs, many=True)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200:foodwithSerializer(many=True)}, request_body=foodwithSerializer)
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = foodwithSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('User_Group_id', openapi.IN_QUERY, description="User_Group_id", type=openapi.TYPE_STRING),
        ],
        responses={200: foodwithSerializer(many=True)}, request_body=foodwithSerializer
    )
    def put(self, request, *args, **kwargs):
        User_Group_id = request.query_params.get('User_Group_id', None)
        User_Group = get_object_or_404(Ticket, pk=User_Group_id)

        serializer = foodwithSerializer(ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        print(request.data)
        serializer.save()
        return Response(
            {"desc": serializers.data},
            status=status.HTTP_200_OK
        )
#chat
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .models import Thread


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)