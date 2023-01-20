from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

occupation_choices = (('owner', 'owner'),
                      ('manager', 'manager')

                      )


class VendorRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    mobile = serializers.CharField(write_only=True, required=True)

    full_name = serializers.CharField(write_only=True, required=True)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    occupation = serializers.ChoiceField(choices=occupation_choices)

    class Meta:
        model = User
        fields = ('full_name', 'occupation', 'mobile', 'email', 'password')

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            occupation=validated_data['occupation'],
            mobile=validated_data['mobile'],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user


# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class UserRegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#             'password2',
#         ]
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'password2': {'write_only': True},
#         }
#
#     def create(self, validated_data):
#         username = validated_data.get('username')
#         email = validated_data.get('email')
#         password = validated_data.get('password')
#         password2 = validated_data.get('password2')
#
#         if password == password2:
#             user = User(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             return user
#         else:
#             raise serializers.ValidationError({
#                 'error': 'Both passwords do not match'
#             })
# customer registration
class CustomerRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    mobile = serializers.CharField(write_only=True, required=True)

    full_name = serializers.CharField(write_only=True, required=True)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    address = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('full_name', 'mobile', 'email', 'password', 'address')

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            address=validated_data['address'],
            mobile=validated_data['mobile'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# change password
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


vendor_choices = (
    ('venue', 'venue'),
    ('food', 'food'),
    ('makeup', 'makeup'),
    ('luxury_car', 'luxury_car'),
    ('music', 'music'),
    ('camera', 'camera'),
    ('decoration', 'decoration'),
    ('fashion', 'fashion'),

)


class vendortypeSerializer(serializers.ModelSerializer):
    vendor_type = serializers.ChoiceField(
        choices=vendor_choices)

    class Meta:
        model = vendortype
        fields = [
            'vendor_type',
            'name_of_business',
            'Owner_name',
            'location',
            # 'first_name',
            # 'last_name',

        ]

    def create(self, validated_data):
        vendor_type = validated_data.get('vendor_type')

        name_of_business = validated_data.get('name_of_business')
        Owner_name = validated_data.get('Owner_name')
        location = validated_data.get('location')

        user = vendortype(vendor_type=vendor_type, name_of_business=name_of_business, Owner_name=Owner_name,
                          location=location)

        user.save()
        return user


# vendor_details
class vendorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorInfo
        fields = [
            'aadhar_no',
            'aadhar_attachment',
            'pan_no',
            'pan_attachment',
            'voter_no',
            'voter_attachment'
            # 'first_name',
            # 'last_name',

        ]

    def create(self, validated_data):
        aadhar_no = validated_data.get('aadhar_no')

        aadhar_attachment = validated_data.get('aadhar_attachment')
        pan_no = validated_data.get('pan_no')
        pan_attachment = validated_data.get('pan_attachment')
        voter_no = validated_data.get('voter_no')

        voter_attachment = validated_data.get('voter_attachment')

        user = VendorInfo(aadhar_no=aadhar_no, aadhar_attachment=aadhar_attachment, pan_no=pan_no,
                          pan_attachment=pan_attachment, voter_no=voter_no, voter_attachment=voter_attachment)

        user.save()
        return user


class Aboutpageserializer(serializers.ModelSerializer):
    class Meta:
        model = about
        fields = [
            'intro',

            # 'first_name',
            # 'last_name',

        ]

    def create(self, validated_data):
        intro = validated_data.get('intro')

        user = about(intro=intro)

        user.save()
        return user


# multiple image

# class imageserializer(serializers.ModelSerializer):
#     images = serializers.ListField(
#         child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
#         write_only=True)
#
#     class Meta:
#         model = ProImage
#         fields = ["uploaded_images"]
#
#         def create(self, validated_data):
#             uploaded_images = validated_data.pop("uploaded_images")
#
#             for image in uploaded_images:
#                 newproduct_image = ProImage.objects.create( image=image)
#             return ProImage
# class MultipleImageSerializer(serializers.Serializer):
#     # class Meta:
#     #     model = ImageModel
#     #     fields = "__all__"
#     images = serializers.ListField(
#         child=serializers.ImageField()
#     )
# car
class carmicropageserializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'imager',
            'company_name',
            'car_name',
            'model',
            'year',
            'rent',
            'fuel_type',
            'seating_capacity',
            'milege',
            'engine',

            # 'first_name',
            # 'last_name',

        ]

    def create(self, validated_data):
        imager = validated_data.get('imager')
        company_name = validated_data.get('company_name')
        car_name = validated_data.get('car_name')
        model = validated_data.get('model')
        year = validated_data.get('year')
        rent = validated_data.get('rent')
        fuel_type = validated_data.get('fuel_type')
        seating_capacity = validated_data.get('seating_capacity')
        milege = validated_data.get('milege')
        engine = validated_data.get('engine')

        user = Car(imager=imager, company_name=company_name, car_name=car_name, model=model, year=year, rent=rent,
                   fuel_type=fuel_type, seating_capacity=seating_capacity, milege=milege, engine=engine)

        user.save()
        return user


# add pictures
class addpicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'image6',
            'image7',
            # 'first_name',
            # 'last_name',

        ]

    def create(self, validated_data):
        image1 = validated_data.get('image1')

        image2 = validated_data.get('image2')
        image3 = validated_data.get('image3')
        image4 = validated_data.get('image4')

        image5 = validated_data.get('image5')
        image6 = validated_data.get('image6')
        image7 = validated_data.get('image7')

        user = Image(image1=image1, image2=image2, image3=image3, image4=image4, image5=image5, image6=image6,
                     image7=image7)

        user.save()
        return user


# venue services
class venueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = [
            'booking_price',
            'tax_rate',
            'max_invitees',

        ]

    def create(self, validated_data):
        booking_price = validated_data.get('booking_price')

        tax_rate = validated_data.get('tax_rate')

        max_invitees = validated_data.get('max_invitees')

        user = Venue(booking_price=booking_price, tax_rate=tax_rate, max_invitees=max_invitees)

        user.save()
        return user


# catering services
class cateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = [
            'price_per_plate',
            'tax_rate',
            'discounted_price',

        ]

    def create(self, validated_data):
        price_per_plate = validated_data.get('price_per_plate')

        tax_rate = validated_data.get('tax_rate')

        discounted_price = validated_data.get('discounted_price')

        user = Catering(price_per_plate=price_per_plate, tax_rate=tax_rate, discounted_price=discounted_price)

        user.save()
        return user


# combined services
class vanuecateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = venuecateringcombined
        fields = [
            'booking_price',
            'max_invitees',
            'price_per_plate',
            'tax_rate',
            'discounted_price',

        ]

    def create(self, validated_data):
        booking_price = validated_data.get('booking_price')
        max_invitees = validated_data.get('max_invitees')

        price_per_plate = validated_data.get('price_per_plate')

        tax_rate = validated_data.get('tax_rate')

        discounted_price = validated_data.get('discounted_price')

        user = venuecateringcombined(booking_price=booking_price, max_invitees=max_invitees,
                                     price_per_plate=price_per_plate, tax_rate=tax_rate,
                                     discounted_price=discounted_price)

        user.save()
        return user


# dropimage in everysection
class dropimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = displayImage
        fields = [
            'Image1',
            'Image2',
            'Image3',
            'Image4',

            # 'first_name',
            # 'last_name',

        ]

    def create(self, validated_data):
        Image1 = validated_data.get('Image1')

        Image2 = validated_data.get('Image2')
        Image3 = validated_data.get('iImage3')
        Image4 = validated_data.get('Image4')

        user = displayImage(Image1=Image1, Image2=Image2, Image3=Image3, Image4=Image4)

        user.save()
        return user


# music services
class djSerializer(serializers.ModelSerializer):
    class Meta:
        model = dj
        fields = [
            'Booking_price',
            'tax_rate',
            'total_hour',
            'discount_rate',

        ]

    def create(self, validated_data):
        Booking_price = validated_data.get('Booking_price')

        tax_rate = validated_data.get('tax_rate')
        total_hour = validated_data.get('total_hour')

        discount_rate = validated_data.get('discount_rate')

        user = dj(Booking_price=Booking_price, tax_rate=tax_rate, total_hour=total_hour,
                  discount_rate=discount_rate)

        user.save()
        return user
class dholSerializer(serializers.ModelSerializer):
    class Meta:
        model = dhol
        fields = [
            'price_of_1_dhol',
            'tax_rate',

            'discount_rate',

        ]

    def create(self, validated_data):
        price_of_1_dhol = validated_data.get('price_of_1_dhol')

        tax_rate = validated_data.get('tax_rate')


        discount_rate = validated_data.get('discount_rate')

        user = dhol(price_of_1_dhol=price_of_1_dhol, tax_rate=tax_rate,
                  discount_rate=discount_rate)

        user.save()
        return user
#camera services
#portpolio camera services
class portpolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = portpolio_package
        fields = [
            'package_name',
            'package_intro',

            'package_price',
            'location',
            'duration',
            'indoor_outdoor_shoot',
            'styling_makeup',
            'costume',
            'intro_video',
            'portpolio_book',
            'poster_size_print',
            'comp_card',
            'visiting_card_of_model',

        ]

    def create(self, validated_data):
        package_name = validated_data.get('package_name')

        package_intro = validated_data.get('package_intro')


        package_price = validated_data.get('package_price')
        location = validated_data('location')
        duration = validated_data('duration')
        indoor_outdoor_shoot = validated_data('indoor_outdoor_shoot')
        costume = validated_data('costume')
        intro_video = validated_data('intro_video')
        portpolio_book = validated_data('portpolio_book')
        poster_size_print = validated_data('poster_size_print')
        comp_card = validated_data('comp_card')
        visiting_card_of_model = validated_data('visiting_card_of_model')

        user = portpolio_package(package_name=package_name,package_intro=package_intro ,package_price=package_price,location=location, duration=duration,indoor_outdoor_shoot=indoor_outdoor_shoot, costume=costume,
                  intro_video=intro_video,portpolio_book=portpolio_book,poster_size_print=poster_size_print,comp_card=comp_card,  visiting_card_of_model=visiting_card_of_model)

        user.save()
        return user
#only engagement services
class engagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price= validated_data.get('package_price')
        package_description=validated_data.get('package_description')




        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = Engagement( package_price= package_price,package_description=package_description,
                  discounted_price=discounted_price,tax_rate=tax_rate )

        user.save()
        return user
#only prewedding
class preweddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = prewedding
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price = validated_data.get('package_price')
        package_description = validated_data.get('package_description')

        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = prewedding(package_price=package_price, package_description=package_description,
                          discounted_price=discounted_price, tax_rate=tax_rate)

        user.save()
        return user
#only wedding
class weddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = wedding
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price = validated_data.get('package_price')
        package_description = validated_data.get('package_description')

        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = wedding(package_price=package_price, package_description=package_description,
                          discounted_price=discounted_price, tax_rate=tax_rate)

        user.save()
        return user
#all 3 services
class allweddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = combined
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price = validated_data.get('package_price')
        package_description = validated_data.get('package_description')

        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = combined(package_price=package_price, package_description=package_description,
                          discounted_price=discounted_price, tax_rate=tax_rate)

        user.save()
        return user
#makeup services
class engagementmakeupSerializer(serializers.ModelSerializer):
    class Meta:
        model = engmakeup
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price= validated_data.get('package_price')
        package_description=validated_data.get('package_description')




        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = engmakeup( package_price= package_price,package_description=package_description,
                  discounted_price=discounted_price,tax_rate=tax_rate )

        user.save()
        return user
#only prewedding
class preweddingmakeupSerializer(serializers.ModelSerializer):
    class Meta:
        model = preweddingmakeup
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price = validated_data.get('package_price')
        package_description = validated_data.get('package_description')

        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = preweddingmakeup(package_price=package_price, package_description=package_description,
                          discounted_price=discounted_price, tax_rate=tax_rate)

        user.save()
        return user
#only wedding
class weddingmakeupSerializer(serializers.ModelSerializer):
    class Meta:
        model = weddingmakeup
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price = validated_data.get('package_price')
        package_description = validated_data.get('package_description')

        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = weddingmakeup(package_price=package_price, package_description=package_description,
                          discounted_price=discounted_price, tax_rate=tax_rate)

        user.save()
        return user
#all 3 services
class allweddingmakeupSerializer(serializers.ModelSerializer):
    class Meta:
        model = allmakeup
        fields = [
            'package_price',
            'package_description',

            'discounted_price',
            'tax_rate',

        ]

    def create(self, validated_data):
        package_price = validated_data.get('package_price')
        package_description = validated_data.get('package_description')

        discounted_price = validated_data.get('discounted_price')
        tax_rate = validated_data.get('tax_rate')

        user = allmakeup(package_price=package_price, package_description=package_description,
                          discounted_price=discounted_price, tax_rate=tax_rate)

        user.save()
        return user
#food services
class foodplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_per_plate
        fields = [
            'price_per_plate',


            'discount_rate',
            'tax_rate',

        ]

    def create(self, validated_data):
        price_per_plate= validated_data.get('price_per_plate')


        discount_rate = validated_data.get('discount_rate')
        tax_rate = validated_data.get('tax_rate')

        user = food_per_plate(price_per_plate=price_per_plate,
                          discount_rate=discount_rate, tax_rate=tax_rate)

        user.save()
        return user
#food without material
class foodwithoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = catering_without_material
        fields = [
            'price_per_25person',

            'discount_rate',
            'tax_rate',

        ]

    def create(self, validated_data):
        price_per_25person = validated_data.get('price_per_25person')

        discount_rate = validated_data.get('discount_rate')
        tax_rate = validated_data.get('tax_rate')

        user = catering_without_material(price_per_25person=price_per_25person,
                              discounte_rate=discount_rate, tax_rate=tax_rate)

        user.save()
        return user
#food with material
class foodwithSerializer(serializers.ModelSerializer):
    class Meta:
        model = catering_with_material
        fields = [
            'price_per_25person',

            'discount_rate',
            'tax_rate',

        ]

    def create(self, validated_data):
        price_per_25person = validated_data.get('price_per_25person')

        discount_rate = validated_data.get('discount_rate')
        tax_rate = validated_data.get('tax_rate')

        user = catering_with_material(price_per_25person=price_per_25person,
                              discount_rate=discount_rate, tax_rate=tax_rate)

        user.save()
        return user