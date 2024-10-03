from django.db import models
from django.utils.translation import gettext as _


PROPERTY_TYPE_CHOICES = (
    ('apartment', _("Piso")),
    ('attic', _("Ático")),
    ('duplex', _("Dúplex")),
    ('independent', _("Chalet independiente")),
    ('semi_detached', _("Chalet adosado")),
    ('rustic', _("Casa rústica")),
)

PROPERTY_EQUIPMENT_CHOICES = (
    ('none', _('Vacío')),
    ('kitchen', 'Sólo cocina equipada'),
    ('furnished', 'Amueblado'),
)

PROPERTY_GOOD_CONDITION_CHOICES = (
    ('new', 'Obra nueva'),
    ('good_condition', 'Buen estado'),
    ('to_reform', 'A reformar'),
)

PROPERTY_FLOOR_CHOICES = (
    ('ground_floor', 'Planta baja'),
    ('1', 'Planta primera'),
    ('2', 'Planta segunda'),
    ('3', 'Planta tercera'),
    ('4', 'Planta cuarta'),
    ('5', 'Planta quinta'),
)

PROPERTY_ENERGY_CERTIFICATE_CHOICES = (
    ('unavailable', 'Aún no disponible'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
    ('G', 'G'),
    ('in_progress', 'En trámite'),
    ('exempt', 'Inmueble exento'),
)

PROPERTY_PRICE_UNIT_CHOICES = (
    ('euro', '€'),
    ('euro_per_month', _('€/mes'))
)

PROPERTY_DEPOSIT_CHOICES = (
    ('one_month', '1 mes'),
    ('two_months', '2 meses'),
    ('three_months', '3 meses'),
)

ROOM_BED_TYPE_CHOICES = (
    ('single', 'Individual'),
    ('double', 'Doble'),
    ('two', 'Dos camas'),
    ('no_bed', 'Sin cama'),
)

ROOM_VIEWS_CHOICES = (
    ('street', 'Ventana a la calle'),
    ('yard', 'Ventana al patio'),
    ('no_window', 'Sin ventana'),
)

ROOM_GENDER_OF_TENANTS = (
    ('both', 'Chicos y chicas'),
    ('male', 'Sólo chicos'),
    ('female', 'Sólo chicas'),
)

ROOM_HOUSE_ENVIRONMENT_CHOICES = (
    ('quiet', 'Tranquilo'),
    ('friendly', 'Amistoso'),
    ('lively', 'Animado'),
)

ROOM_TENANT_GENDER_CHOICES = (
    ('indifferent', 'Indiferente'),
    ('male', 'Chico'),
    ('female', 'Chica'),
)

ROOM_TENANT_OCCUPATION_CHOICES = (
    ('indifferent', 'Indiferente'),
    ('student', 'Estudiante'),
    ('worker', 'Con trabajo'),
)


class ApartmentRent(models.Model):
    featured = models.IntegerField(default=0)
    address = models.CharField(max_length=1000, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    pic = models.ImageField(upload_to='medios', default='img1.jpg')
    pic_thumbnail = models.ImageField(upload_to='medios', default='img1.jpg')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    price_units = models.CharField(max_length=20, default=_('euro_per_month'))
    deposit = models.CharField(max_length=30, choices=PROPERTY_DEPOSIT_CHOICES, blank=True)
    size = models.IntegerField(blank=True, null=True)
    size_net = models.IntegerField(blank=True, null=True)
    energy_certificate = models.CharField(max_length=30, choices=PROPERTY_ENERGY_CERTIFICATE_CHOICES, blank=True)
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES, default='apartment')
    equipment = models.CharField(max_length=100, choices=PROPERTY_EQUIPMENT_CHOICES, default='furnished')
    n_rooms = models.IntegerField(default=1)
    n_bathrooms = models.IntegerField(default=1)
    good_condition = models.CharField(max_length=100, choices=PROPERTY_GOOD_CONDITION_CHOICES, default='good_condition')
    pets_allowed = models.BooleanField(default=True)
    air_conditioning = models.BooleanField(default=True)
    builtin_wardrobes = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    storage_room = models.BooleanField(default=False)
    luxury = models.BooleanField(default=False)
    floor = models.CharField(max_length=100, choices=PROPERTY_FLOOR_CHOICES, default='ground_floor')
    wifi = models.BooleanField(default=True)

    def __str__(self):
        return f"Apartment (rent) {self.id} - {self.address}"

    @property
    def title(self):
        return f"Piso en {self.address}"


class Room(models.Model):
    featured = models.IntegerField(default=0)
    address = models.CharField(max_length=1000, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    pic = models.ImageField(upload_to='medios', default='img1.jpg')
    pic_thumbnail = models.ImageField(upload_to='medios', default='img1.jpg')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    price_unit = models.CharField(max_length=20, choices=PROPERTY_PRICE_UNIT_CHOICES, default=_('euro_per_month'))
    deposit = models.CharField(max_length=30, choices=PROPERTY_DEPOSIT_CHOICES, blank=True)
    property_size = models.IntegerField(blank=True, null=True)
    room_size = models.IntegerField(blank=True, null=True)
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES, default='apartment')
    n_rooms = models.IntegerField(default=1)
    n_bathrooms = models.IntegerField(default=1)
    good_condition = models.CharField(max_length=100, choices=PROPERTY_GOOD_CONDITION_CHOICES, default='good_condition')
    air_conditioning = models.BooleanField(default=True)
    builtin_wardrobes = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    floor = models.CharField(max_length=100, choices=PROPERTY_FLOOR_CHOICES, default='ground_floor')
    smoking_allowed = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    couples_allowed = models.BooleanField(default=False)
    cleaning_included = models.BooleanField(default=False)
    building_doorman = models.BooleanField(default=False)
    building_garden = models.BooleanField(default=False)
    building_swimming_pool = models.BooleanField(default=False)
    room_bed_type = models.CharField(max_length=20, choices=ROOM_BED_TYPE_CHOICES, default='single')
    room_views = models.CharField(max_length=20, choices=ROOM_VIEWS_CHOICES, default='street')
    furnished = models.BooleanField(default=True)
    private_badroom = models.BooleanField(default=False)
    available_from = models.DateField(blank=True, null=True)
    n_people = models.IntegerField(default=2)
    someone_living = models.BooleanField(default=True)
    people_age_range_lower = models.IntegerField(blank=True, null=True)
    people_age_range_upper = models.IntegerField(blank=True, null=True)
    gender_of_tenants = models.CharField(max_length=20, choices=ROOM_GENDER_OF_TENANTS, default='both')
    tenants_are_students = models.BooleanField(default=False)
    tenants_are_workers = models.BooleanField(default=False)
    landlord_lives_in_the_house = models.BooleanField(default=False)
    house_environment = models.CharField(max_length=20, choices=ROOM_HOUSE_ENVIRONMENT_CHOICES, default='quiet')
    tenant_gender = models.CharField(max_length=20, choices=ROOM_TENANT_GENDER_CHOICES, default='indifferent')
    tenant_age_range_lower = models.IntegerField(blank=True, null=True)
    tenant_age_range_upper = models.IntegerField(blank=True, null=True)
    tenant_occupation = models.CharField(max_length=20, choices=ROOM_TENANT_OCCUPATION_CHOICES, default='indifferent')

    def __str__(self):
        return f"Room {self.id} - {self.address}"

    @property
    def title(self):
        return f"Habitación en {self.address}"


class ApartmentSale(models.Model):
    featured = models.IntegerField(default=0)
    address = models.CharField(max_length=1000, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    pic = models.ImageField(upload_to='medios', default='img1.jpg')
    pic_thumbnail = models.ImageField(upload_to='medios', default='img1.jpg')
    description = models.TextField(blank=True)
    price = models.CharField(max_length=50)
    price_units = models.CharField(max_length=20, default=_('euro'))
    size = models.IntegerField(blank=True, null=True)
    size_net = models.IntegerField(blank=True, null=True)
    energy_certificate = models.CharField(max_length=30, choices=PROPERTY_ENERGY_CERTIFICATE_CHOICES, blank=True)
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES, default='apartment')
    n_rooms = models.IntegerField()
    n_bathrooms = models.IntegerField(default=1)
    good_condition = models.CharField(max_length=100, choices=PROPERTY_GOOD_CONDITION_CHOICES, default='good_condition')
    air_conditioning = models.BooleanField(default=True)
    builtin_wardrobes = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    storage_room = models.BooleanField(default=False)
    luxury = models.BooleanField(default=False)
    floor = models.CharField(max_length=100, choices=PROPERTY_FLOOR_CHOICES, default='ground_floor')

    def __str__(self):
        return f"Apartment (sale) {self.id} - {self.address}"

    @property
    def title(self):
        return f"Piso en {self.address}"
