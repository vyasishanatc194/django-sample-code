# Generated by Django 3.1.5 on 2021-02-12 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AspectsMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, help_text='Date when deleted', null=True, verbose_name='Deleted At')),
                ('delete_reason', models.CharField(blank=True, default=None, help_text='Delete Reason', max_length=300, null=True, verbose_name='Delete Reason')),
                ('name', models.CharField(help_text='Aspect name', max_length=255, verbose_name='Aspect name')),
                ('aspect_type', models.CharField(blank=True, choices=[('1', 'Closed'), ('2', 'Open')], help_text='Aspect meta data type', max_length=128, null=True, verbose_name='Aspect meta data type')),
                ('aspect_input_type', models.CharField(blank=True, choices=[('1', 'Single'), ('2', 'Multi')], help_text='Aspect meta data input type', max_length=128, null=True, verbose_name='Aspect meta data input type')),
                ('is_model_aspect', models.BooleanField(default=False, help_text='Is Model Aspect?', verbose_name='Is Model Aspect?')),
                ('model_title_order', models.IntegerField(blank=True, default=None, help_text='Model Title Order', null=True, verbose_name='Model Title Order')),
                ('model_title_text_before_aspect', models.CharField(blank=True, help_text='Model Title Text Before Aspect', max_length=255, null=True, verbose_name='Model Title Text Before Aspect')),
                ('model_title_text_after_aspect', models.CharField(blank=True, help_text='Model Title Text After Aspect', max_length=255, null=True, verbose_name='Model Title Text After Aspect')),
                ('my_roga_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspect_meta_data_my_roga_category', to='home.myrogacategory')),
            ],
            options={
                'verbose_name': 'Aspects Meta Data',
                'verbose_name_plural': 'Aspects Meta Data',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AspectValuesMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, help_text='Date when deleted', null=True, verbose_name='Deleted At')),
                ('delete_reason', models.CharField(blank=True, default=None, help_text='Delete Reason', max_length=300, null=True, verbose_name='Delete Reason')),
                ('value_name', models.CharField(help_text='Value Name', max_length=255, verbose_name='Value Name')),
                ('normalized_aspect_value', models.CharField(blank=True, help_text='Normalized Aspect Value', max_length=255, null=True, verbose_name='Normalized Aspect Value')),
                ('value_type', models.CharField(blank=True, choices=[('1', 'Text'), ('2', 'Number')], help_text='Value type', max_length=128, null=True, verbose_name='Value type')),
                ('aspect_meta_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspect_values_meta_data', to='product.aspectsmetadata')),
                ('my_roga_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspect_values_my_roga_category', to='home.myrogacategory')),
            ],
            options={
                'verbose_name': 'Aspect Values Meta Data',
                'verbose_name_plural': 'Aspect Values Meta Data',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, help_text='Date when deleted', null=True, verbose_name='Deleted At')),
                ('delete_reason', models.CharField(blank=True, default=None, help_text='Delete Reason', max_length=300, null=True, verbose_name='Delete Reason')),
                ('title', models.CharField(blank=True, help_text='Product title', max_length=255, null=True, verbose_name='Product title')),
                ('description', models.TextField(blank=True, help_text='Product Description', null=True, verbose_name='Product Description')),
                ('product_status', models.CharField(blank=True, choices=[('1', 'Live'), ('2', 'Deleted')], help_text='Product Status', max_length=128, null=True, verbose_name='Product Status')),
                ('product_stealth', models.CharField(blank=True, help_text='Product Stealth', max_length=50, null=True, verbose_name='Product Stealth')),
                ('image_url', models.TextField(blank=True, help_text='Product Image URL', null=True, verbose_name='Product Image URL')),
                ('review_url', models.TextField(blank=True, help_text='Review URL', null=True, verbose_name='Review URL')),
                ('review_count', models.IntegerField(blank=True, default=0, help_text='Review Count', null=True, verbose_name='Review Count')),
                ('review_score', models.FloatField(blank=True, default=0, help_text='Review Score', max_length=11, null=True, verbose_name='Review Score')),
                ('hero_offer_url', models.TextField(blank=True, help_text='Hero Offer URL', null=True, verbose_name='Hero Offer URL')),
                ('hero_offer_price', models.FloatField(blank=True, default=0, help_text='Hero Offer Price', max_length=11, null=True, verbose_name='Hero Offer Price')),
                ('second_hero_offer_url', models.TextField(blank=True, help_text='Second Hero Offer URL', null=True, verbose_name='Second Hero Offer URL')),
                ('second_hero_offer_price', models.FloatField(blank=True, default=0, help_text='Second Hero Offer Price', max_length=11, null=True, verbose_name='Second Hero Offer Price')),
                ('hero_offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_hero_offer', to='offer.offer')),
                ('hero_offer_market_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hero_offer_market_place', to='home.marketplace')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_language', to='home.language')),
                ('my_roga_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_my_roga_category', to='home.myrogacategory')),
                ('second_hero_offer_market_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_hero_offer_market_place', to='home.marketplace')),
                ('second_offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_second_offer', to='offer.offer')),
                ('technical_aspect_values', models.ManyToManyField(related_name='product_technical_aspect_values', to='product.AspectValuesMetaData')),
                ('technical_aspects', models.ManyToManyField(related_name='product_technical_aspects', to='product.AspectsMetaData')),
            ],
            options={
                'verbose_name': 'Product Catalog',
                'verbose_name_plural': 'Product Catalog',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AggregationModelSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, help_text='Date when deleted', null=True, verbose_name='Deleted At')),
                ('delete_reason', models.CharField(blank=True, default=None, help_text='Delete Reason', max_length=300, null=True, verbose_name='Delete Reason')),
                ('aspects', models.ManyToManyField(related_name='aggregation_technical_aspects', to='product.AspectsMetaData')),
                ('my_roga_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aggregation_my_roga_category', to='home.myrogacategory')),
            ],
            options={
                'verbose_name': 'Aggregation Model Set',
                'verbose_name_plural': 'Aggregation Model Sets',
                'ordering': ['-created_at'],
            },
        ),
    ]
