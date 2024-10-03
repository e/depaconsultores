# Generated by Django 5.1.1 on 2024-09-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=1000)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('pic', models.ImageField(default='img1.jpg', upload_to='medios')),
                ('description', models.TextField(blank=True)),
                ('price_rent', models.IntegerField()),
                ('size', models.IntegerField(blank=True, null=True)),
                ('property_type', models.CharField(choices=[('apartment', 'Piso'), ('attic', 'Ático'), ('duplex', 'Dúplex'), ('independent', 'Chalet independiente'), ('semi_detached', 'Chalet adosado'), ('rustic', 'Casa rústica')], default='apartment', max_length=100)),
                ('equipment', models.CharField(choices=[('none', 'Vacío'), ('kitchen', 'Sólo cocina equipada'), ('furnished', 'Amueblado')], default='furnished', max_length=100)),
                ('n_rooms', models.IntegerField(default=1)),
                ('n_bathrooms', models.IntegerField(default=1)),
                ('good_condition', models.CharField(choices=[('new', 'Obra nueva'), ('good_condition', 'Buen estado'), ('to_reform', 'A reformar')], default='good_condition', max_length=100)),
                ('pets_allowed', models.BooleanField(default=True)),
                ('air_conditioning', models.BooleanField(default=True)),
                ('builtin_wardrobes', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('terrace', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('garage', models.BooleanField(default=False)),
                ('garden', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('storage_room', models.BooleanField(default=False)),
                ('luxury', models.BooleanField(default=False)),
                ('floor', models.CharField(choices=[('ground_floor', 'Planta baja'), ('1', 'Planta primera'), ('2', 'Planta segunda'), ('3', 'Planta tercera'), ('4', 'Planta cuarta'), ('5', 'Planta quinta')], default='ground_floor', max_length=100)),
                ('wifi', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=1000)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('price_sale', models.CharField(max_length=50)),
                ('n_rooms', models.IntegerField()),
                ('has_garage', models.BooleanField(default=False)),
                ('has_garden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=1000)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('pic', models.ImageField(default='img1.jpg', upload_to='medios')),
                ('description', models.TextField(blank=True)),
                ('price_room', models.IntegerField()),
                ('deposit', models.CharField(blank=True, max_length=30)),
                ('property_size', models.IntegerField(blank=True, null=True)),
                ('room_size', models.IntegerField(blank=True, null=True)),
                ('property_type', models.CharField(choices=[('apartment', 'Piso'), ('attic', 'Ático'), ('duplex', 'Dúplex'), ('independent', 'Chalet independiente'), ('semi_detached', 'Chalet adosado'), ('rustic', 'Casa rústica')], default='apartment', max_length=100)),
                ('n_rooms', models.IntegerField(default=1)),
                ('n_bathrooms', models.IntegerField(default=1)),
                ('good_condition', models.CharField(choices=[('new', 'Obra nueva'), ('good_condition', 'Buen estado'), ('to_reform', 'A reformar')], default='good_condition', max_length=100)),
                ('air_conditioning', models.BooleanField(default=True)),
                ('builtin_wardrobes', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('terrace', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('floor', models.CharField(choices=[('ground_floor', 'Planta baja'), ('1', 'Planta primera'), ('2', 'Planta segunda'), ('3', 'Planta tercera'), ('4', 'Planta cuarta'), ('5', 'Planta quinta')], default='ground_floor', max_length=100)),
                ('smoking_allowed', models.BooleanField(default=False)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('couples_allowed', models.BooleanField(default=False)),
                ('cleaning_included', models.BooleanField(default=False)),
                ('building_doorman', models.BooleanField(default=False)),
                ('building_garden', models.BooleanField(default=False)),
                ('building_swimming_pool', models.BooleanField(default=False)),
                ('room_bed_type', models.CharField(choices=[('single', 'Individual'), ('double', 'Doble'), ('two', 'Dos camas'), ('no_bed', 'Sin cama')], default='single', max_length=20)),
                ('room_views', models.CharField(choices=[('street', 'Ventana a la calle'), ('yard', 'Ventana al patio'), ('no_window', 'Sin ventana')], default='street', max_length=20)),
                ('furnished', models.BooleanField(default=True)),
                ('private_badroom', models.BooleanField(default=False)),
                ('available_from', models.DateField(blank=True, null=True)),
                ('n_people', models.IntegerField(default=2)),
                ('someone_living', models.BooleanField(default=True)),
                ('people_age_range_lower', models.IntegerField(blank=True, null=True)),
                ('people_age_range_upper', models.IntegerField(blank=True, null=True)),
                ('gender_of_tenants', models.CharField(choices=[('both', 'Chicos y chicas'), ('male', 'Sólo chicos'), ('female', 'Sólo chicas')], default='both', max_length=20)),
                ('tenants_are_students', models.BooleanField(default=False)),
                ('tenants_are_workers', models.BooleanField(default=False)),
                ('landlord_lives_in_the_house', models.BooleanField(default=False)),
                ('house_environment', models.CharField(choices=[('quiet', 'Tranquilo'), ('friendly', 'Amistoso'), ('lively', 'Animado')], default='quiet', max_length=20)),
                ('tenant_gender', models.CharField(choices=[('indifferent', 'Indiferente'), ('male', 'Chico'), ('female', 'Chica')], default='indifferent', max_length=20)),
                ('tenant_age_range_lower', models.IntegerField(blank=True, null=True)),
                ('tenant_age_range_upper', models.IntegerField(blank=True, null=True)),
                ('tenant_occupation', models.CharField(choices=[('indifferent', 'Indiferente'), ('student', 'Estudiante'), ('worker', 'Con trabajo')], default='indifferent', max_length=20)),
            ],
        ),
    ]
