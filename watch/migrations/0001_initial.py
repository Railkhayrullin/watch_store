# Generated by Django 3.1.7 on 2021-04-07 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='brand')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='CaseMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='case material')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
            ],
            options={
                'verbose_name': 'case material',
                'verbose_name_plural': 'case materials',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='category')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='country')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='PriceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='brand')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='watch')),
                ('price', models.FloatField(verbose_name='price')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_products', to='watch.brand')),
                ('case_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_material_products', to='watch.casematerial')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='watch.category')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_products', to='watch.country')),
            ],
            options={
                'verbose_name': 'watch',
                'verbose_name_plural': 'watch',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
                ('price_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_type_prices', to='watch.pricetype')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='watch.product')),
            ],
        ),
    ]
