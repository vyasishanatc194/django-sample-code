# Generated by Django 3.1.5 on 2021-02-12 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('offer', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, help_text='Date when deleted', null=True, verbose_name='Deleted At')),
                ('delete_reason', models.CharField(blank=True, default=None, help_text='Delete Reason', max_length=300, null=True, verbose_name='Delete Reason')),
                ('model_aggregation_key', models.TextField(help_text='Model Aggregation Key', verbose_name='Model Aggregation Key')),
                ('hero_product_price', models.FloatField(blank=True, default=0, help_text='Hero Product Price', max_length=11, null=True, verbose_name='Hero Product Price')),
                ('second_hero_product_price', models.FloatField(blank=True, default=0, help_text='Second Hero Product Price', max_length=11, null=True, verbose_name='Second Hero Product Price')),
                ('title', models.CharField(help_text='Model title', max_length=255, verbose_name='Model title')),
                ('description', models.TextField(blank=True, help_text='Model Description', null=True, verbose_name='Model Description')),
                ('description_image_url', models.TextField(blank=True, help_text='Model Description Image URL', null=True, verbose_name='Model Description Image URL')),
                ('model_status', models.CharField(blank=True, choices=[('1', 'Live'), ('2', 'Deleted')], help_text='Model Status', max_length=128, null=True, verbose_name='Model Status')),
                ('model_stealth', models.CharField(blank=True, help_text='Model Stealth', max_length=50, null=True, verbose_name='Model Stealth')),
                ('product_review_count', models.IntegerField(blank=True, default=0, help_text='Product Review Count', null=True, verbose_name='Product Review Count')),
                ('product_review_score', models.FloatField(blank=True, default=0, help_text='Product Review Score', max_length=11, null=True, verbose_name='Product Review Score')),
                ('image_url', models.TextField(blank=True, help_text='Model Image URL', null=True, verbose_name='Model Image URL')),
                ('review_url', models.TextField(blank=True, help_text='Review URL', null=True, verbose_name='Review URL')),
                ('recommendation_score', models.FloatField(blank=True, default=0, help_text='Recommendation Score', max_length=11, null=True, verbose_name='Recommendation Score')),
                ('aggregation_model_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aggregation_model_catalog', to='product.aggregationmodelset')),
                ('hero_offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_catalog_hero_offer', to='offer.offer')),
                ('hero_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_catalog_hero_product', to='product.productcatalog')),
                ('hero_product_market_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hero_product_market_place', to='home.marketplace')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_catalog_language', to='home.language')),
                ('my_roga_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_catalog_my_roga_category', to='home.myrogacategory')),
                ('product_catalog', models.ManyToManyField(related_name='model_catalog_products', to='product.ProductCatalog')),
                ('second_hero_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_catalog_second_hero_product', to='product.productcatalog')),
                ('second_hero_product_market_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_hero_product_market_place', to='home.marketplace')),
                ('second_offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model_catalog_second_offer', to='offer.offer')),
            ],
            options={
                'verbose_name': 'Model Catalog',
                'verbose_name_plural': 'Model Catalog',
                'ordering': ['-created_at'],
            },
        ),
    ]
