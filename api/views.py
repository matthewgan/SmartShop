from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from api.models import *
from api.serializers import *
from api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
import requests
from rest_framework.decorators import authentication_classes, permission_classes
import uuid
from django.http import JsonResponse
from django.http import Http404

class WUserCreateOrListView(APIView):
    """
    List all the wechat users, or create a new user
    """
    def get(self, request, *args, **kwargs):
        """
        List all the wechat user in the database
        Need to add permission control later
        Only show to shop owners and system admins
        """
        wusers = WUser.objects.all()
        serializer = WUserListSerializer(wusers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Receive post message from wechat mini app,
        check if user is new to create a new user,
        else search the database and reply user's uuid and infos
        """
        serializer = WUserLoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            # Use code to Request wxid and sessionkey from wechat API
            # appid and secret from wechat miniapp website
            wxapp_secret = 'e90efc114a06215f1c9ddac8dcf70d4e'
            wxapp_appid = 'wx77d45362c6c2763e'
            # fixed wechat API address for wx.login
            baseurl = 'https://api.weixin.qq.com/sns/jscode2session?appid='
            content = baseurl + wxapp_appid + '&secret=' + wxapp_secret + '&js_code=' + code + '&grant_type=authorization_code'
            # request wechat API and get json response
            res = requests.get(content).json()
            if res.get('errcode') is not None:
                return Response(res, status=status.HTTP_204_NO_CONTENT)
            else:
                openid = res.get('openid')
                session_key = res.get('session_key')
                # do search on the database to see if the user is already existed
                try:
                    wuser = WUser.objects.get(openid=openid)
                except WUser.DoesNotExist:
                    wuser = serializer.create(serializer.validated_data)
                    wuser.openid = openid
                    wuser.session_key = session_key
                    wuser.save()
                output_serializer = WUserLoginResponseSerializer(wuser)
                return Response(output_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# class OnLogin(APIView):
#     # def get(self, request, format=None):
#     #     return Response(status=status.HTTP_200_OK)
#     def post(self, request, format=None):
#         """
#         Receive code from miniapp,
#         Request wxid and sessionkey from wechat API
#         """
#         # appid and secret from wechat miniapp website
#         secret = 'e90efc114a06215f1c9ddac8dcf70d4e'
#         appid = 'wx77d45362c6c2763e'
#         if request.method == 'POST':
#             code = request.data.get('code')
#             # nickName = request.data.get('userNickname')
#             # avataUrl = request.data.get('userAvatarUrl')
#             # gender = request.data.get('userGender')
#             # city = request.data.get('userCity')
#             # province = request.data.get('userProvince')
#             # country = request.data.get('userCountry')
#             # language = request.data.get('userLanguage')
#             # input value check
#             try:
#                 # fixed wechat API address for wx.login
#                 baseUrl = 'https://api.weixin.qq.com/sns/jscode2session?appid='
#                 extUrl1 = '&secret='
#                 extUrl2 = '&js_code='
#                 extUrl3 = '&grant_type=authorization_code'
#                 content = baseUrl + appid + extUrl1 + secret + extUrl2 + code + extUrl3
#             except ValueError:
#                 return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
#
#             # request wechat API and get json response
#             res = requests.get(content).json()
#             # validation check
#             if res.get('errcode') is not None:
#                 return Response(res, status=status.HTTP_204_NO_CONTENT)
#             else:
#                 openid = res.get('openid')
#                 session_key = res.get('session_key')
#                 return Response(res, status=status.HTTP_200_OK)
#                 # do search in the database
#                 userinfo = Customer.objects.filter(openid=openid)
#                 # new user save to database
#                 # if userinfo is None:
#                 #     # add new user
#                 #     useruuid = uuid.uuid1()
#                     # newuser = Customer.objects.create(openid=openid,
#                     #                                   nickName=nickName,
#                     #                                   avataUrl=avataUrl,
#                     #                                   gender=gender,
#                     #                                   city=city,
#                     #                                   province=province,
#                     #                                   country=country,
#                     #                                   language=language,
#                     #                                   uuid=useruuid)
#                     # newuser.save()
#                     # do search again
#                 #     userinfo = Customer.objects.filter(openid=openid)
#                 #
#                 # # get uuid from database
#                 # ret = {
#                 #     'uuid': userinfo.uuid,
#                 # }
#                 # return Response(userinfo, status=status.HTTP_200_OK)
#
#
# class CustomerViewSet(viewsets.ModelViewSet):
#     """
#         This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#     #                       IsOwnerOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class OwnerViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = OwnerSerializer
#
#
# class WxUserViewSet(viewsets.ModelViewSet):
#     queryset = WxUser.objects.all()
#     serializer_class = WxUserSerializer
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# @authentication_classes([])
# @permission_classes([])
# class ShopViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#
#
# class RackViewSet(viewsets.ModelViewSet):
#     queryset = Rack.objects.all()
#     serializer_class = RackSerializer
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class SupplierViewSet(viewsets.ModelViewSet):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#
#
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ESLViewSet(viewsets.ModelViewSet):
#     queryset = ESL.objects.all()
#     serializer_class = ESLSerializer
#
#
# class RFIDViewSet(viewsets.ModelViewSet):
#     queryset = RFID.objects.all()
#     serializer_class = RFIDSerializer
#
#
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer