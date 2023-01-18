import uuid
from django.db.models import Q
import pytz
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


# Create your models here.
class UserType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


occupation_choices = (('owner', 'owner'),
                      ('manager', 'manager')

                      )


def picture_profile_attachment(instance, filename):
    return f"files/{instance.id}/attchment/{instance.id}_{filename}"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    TIMEZONES = tuple(zip(pytz.common_timezones, pytz.common_timezones))
    occupation = models.CharField(choices=occupation_choices, max_length=15)

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
    )

    mobile = models.CharField(
        max_length=50,
        verbose_name="Contact No.")
    country_code = models.CharField(max_length=10, default='+91')

    # full name
    full_name = models.CharField(max_length=70, null=True, blank=True)

    # address
    address = models.CharField(max_length=70, null=True, blank=True)

    # profile photo
    picture_profile = models.FileField(upload_to=picture_profile_attachment, null=True, blank=True)

    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default="Asia/Kolkata")

    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    # is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    username = None
    REQUIRED_FIELDS = ['mobile']

    objects = CustomUserManager()

    class Meta:
        # unique_together = ('country_code', 'mobile',)
        app_label = "App"


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


class vendortype(models.Model):
    vendor_type = models.CharField(choices=vendor_choices, max_length=15)
    name_of_business = models.CharField(max_length=100)
    Owner_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


def aadhar_attachment(instance, filename):
    return f"files/{instance.business_name}/aadhar/{instance.id}_{filename}"


def voter_attachment(instance, filename):
    return f"files/{instance.business_name}/voter/{instance.id}_{filename}"


def pan_attachment(instance, filename):
    return f"files/{instance.business_name}/pan/{instance.id}_{filename}"


def gst_attchment(instance, filename):
    return f"files/{instance.business_name}/gst/{instance.id}_{filename}"

#profile of user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self):
        super().save()

        img = Image.open(self.image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            img.save(self.image.path)  # Save it again and override the larger image

    # def __str__(self):
    #     return f'{self.user.username} Profile' #show how we want it to be displayed
class VendorInfo(models.Model):
    # id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)

    business_type = models.CharField(max_length=70, null=True, blank=True)
    business_name = models.CharField(max_length=70)

    # type_of_vendor = models.ForeignKey(vendortype, on_delete=models.CASCADE)
    aadhar_no = models.CharField(max_length=50, null=True, blank=True)
    aadhar_attachment = models.FileField(upload_to=aadhar_attachment, null=True, blank=True)

    voter_no = models.CharField(max_length=100, null=True, blank=True)
    voter_attachment = models.FileField(upload_to=voter_attachment, null=True, blank=True)

    pan_no = models.CharField(max_length=50, null=True, blank=True)
    pan_attachment = models.FileField(upload_to=pan_attachment, null=True, blank=True)

    gst_no = models.CharField(max_length=100, null=True, blank=True)
    gst_attchment = models.FileField(upload_to=gst_attchment, null=True, blank=True)

    def __str__(self):
        return f"{self.user.name}"


class about(models.Model):
    user = models.ManyToManyField(User)
    intro = models.TextField()


# luxury car category
car_name_choices = (
    ('Maruti', 'Maruti'),
    ('Hyundai', 'Hyundai'),
    ('Tata', 'Tata'),
    ('Mahindra', 'Mahindra'),
    ('Kia', 'Kia'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Renault', 'Renault'),
    ('Honda', 'Honda'),

    ('MG', 'MG'),
    ('Nissan', 'Nisaan'),
    ('Datsun', 'Datsun'),
    ('Toyota', 'Toyota'),
    ('Honda', 'Honda'),
)
date_choices = (
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2014'),
    ('2016', '2016'),
    ('2017', '2017'),

    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),

)
fuel_choices = (
    ('Diesel', 'Diesel'),
    ('Petrol', 'Petrol')
)
seat_choices = (
    ('3', '3'),
    ('5', '5'),
    ('7', '7'),

)
engine_choices = (
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual')
)


class Car(models.Model):
    user = models.ManyToManyField(User)
    imager = models.ImageField(upload_to="car", default="", null=True, blank=True)
    company_name = models.CharField(max_length=100)
    car_name = models.CharField(choices=car_name_choices, max_length=20)
    model = models.CharField(max_length=100)
    year = models.CharField(choices=date_choices, max_length=4)
    rent = models.IntegerField()
    fuel_type = models.CharField(choices=fuel_choices, max_length=10)
    seating_capacity = models.CharField(choices=seat_choices, max_length=1)
    milege = models.IntegerField()
    engine = models.CharField(choices=engine_choices, max_length=20)


# review model
# class Review(models.Model):
#     product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="reviews")
#     date_created = models.DateTimeField(auto_now_add=True)
#     description = models.TextField(default="description")
#     name = models.CharField(max_length=50)
# #multiple images model
# class ProImage(models.Model):
#     Car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to="img", default="", null=True, blank=True)
#
#     def __str__(self):
#         return self.description
# add pictures
class Image(models.Model):
    user = models.ManyToManyField(User)
    image1 = models.ImageField(upload_to="img", default="", null=False, blank=False)
    image2 = models.ImageField(upload_to="img", default="", null=False, blank=False)
    image3 = models.ImageField(upload_to="img", default="", null=False, blank=False)
    image4 = models.ImageField(upload_to="img", default="", null=False, blank=False)
    image5 = models.ImageField(upload_to="img", default="", null=True, blank=True)
    image6 = models.ImageField(upload_to="img", default="", null=True, blank=True)
    image7 = models.ImageField(upload_to="img", default="", null=True, blank=True)

#venue services
class Venue(models.Model):
    user = models.ManyToManyField(User)
    booking_price = models.IntegerField()
    tax_rate = models.IntegerField()
    max_invitees = models.IntegerField()
class Catering(models.Model):
    user = models.ManyToManyField(User)
    price_per_plate = models.IntegerField()
    tax_rate= models.IntegerField()
    discounted_price = models.IntegerField()
class venuecateringcombined(models.Model):
    user = models.ManyToManyField(User)
    booking_price = models.IntegerField()
    max_invitees = models.IntegerField()
    price_per_plate = models.IntegerField()
    tax_rate = models.IntegerField()
    discounted_price = models.IntegerField()

# display image on homepage
class displayImage(models.Model):
    user = models.ManyToManyField(User)
    Image1 = models.ImageField(upload_to="dimg", default="", null=False, blank=False)
    Image2 = models.ImageField(upload_to="dimg", default="", null=False, blank=False)
    Image3 = models.ImageField(upload_to="dimg", default="", null=False, blank=False)
    Image4 = models.ImageField(upload_to="dimg", default="", null=False, blank=False)
#music services
class dj(models.Model):
    user = models.ManyToManyField(User)

    Booking_price = models.IntegerField()
    tax_rate = models.IntegerField()
    total_hour = models.IntegerField()
    discount_rate = models.IntegerField()
class dhol(models.Model):
    user = models.ManyToManyField(User)
    price_of_1_dhol = models.IntegerField()
    tax_rate = models.IntegerField()
    discount_rate = models.IntegerField()
class musicall(models.Model):
    user = models.ManyToManyField(User)
    Booking_price = models.IntegerField()
    total_hour = models.IntegerField()
    price_of_1_dhol = models.IntegerField()
    tax_rate = models.IntegerField()
    discount_rate = models.IntegerField()


#camera services
class portpolio_package(models.Model):
    user = models.ManyToManyField(User)
    package_name = models.CharField(max_length=200, default=False)
    package_intro = models.TextField(default=False)
    package_price = models.IntegerField(default=False)
    location = models.CharField(max_length=500,default=True)
    duration = models.IntegerField(default=True)
    indoor_outdoor_shoot = models.TextField(max_length=500, default=True)
    styling_makeup= models.TextField(default=True)
    costume = models.TextField(default=True)
    intro_video = models.CharField(default=True, max_length=1000)
    portpolio_book = models.CharField(default=True, max_length=200)
    poster_size_print = models.CharField(default=True, max_length=500)
    comp_card = models.CharField(default=True, max_length=500)
    visiting_card_of_model = models.CharField(default=True, max_length=100)
class Engagement(models.Model):
    user = models.ManyToManyField(User)
    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()
class prewedding(models.Model):
    user = models.ManyToManyField(User)

    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()

class wedding(models.Model):
    user = models.ManyToManyField(User)
    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()
class combined(models.Model):
    user = models.ManyToManyField(User)
    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()

#makeup services
class engmakeup(models.Model):
    user = models.ManyToManyField(User)
    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()

class preweddingmakeup(models.Model):
    user = models.ManyToManyField(User)
    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()
class weddingmakeup(models.Model):
    user = models.ManyToManyField(User)
    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()
class allmakeup(models.Model):
    user = models.ManyToManyField(User)
    package_price = models.IntegerField()
    package_description = models.TextField()
    discounted_price = models.IntegerField()
    tax_rate = models.IntegerField()
#food services
class food_per_plate(models.Model):
    price_per_plate = models.IntegerField()
    tax_rate = models.IntegerField()
    discount_rate = models.IntegerField()
class catering_without_material(models.Model):
    price_per_25person = models.IntegerField()
    tax_rate = models.IntegerField()
    discount_rate = models.IntegerField()
class catering_with_material(models.Model):
    price_per_25person = models.IntegerField()
    tax_rate = models.IntegerField()
    discount_rate = models.IntegerField()
class Notification(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)
    def save(self, *args, **kwars):
        print('save called')
        super(Notification, self).save(*args, **kwars)
#chat
class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)