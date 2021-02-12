import copy
from product.models import AspectsMetaData

PRODUCT_DEFAULT_COLUMNS = ['Product ID', 'Category', 'Product Status', 'Product Stealth', \
        'Language', 'Image URL', 'Review URL', 'Review Count', 'Review Score', 'Hero Offer Url', \
        'Hero Offer Price', 'Hero Offer Marketplace ID', 'Second Offer Url', \
        'Second Offer Price', 'Second Offer Marketplace ID']

PRODUCT_DEFAULT_TECHNICAL_ASPECTS = ['Title', 'Brand', 'Model', 'MPN', 'UPC', 'ASIN']

def get_formatted_products(categories, products, selected_category, selected_product):
    DEFAULT_COLUMNS = copy.deepcopy(PRODUCT_DEFAULT_COLUMNS)
    TECHNICAL_ASPECTS = copy.deepcopy(PRODUCT_DEFAULT_TECHNICAL_ASPECTS)

    if selected_category:
        records = products.filter(my_roga_category=selected_category)
        selected_category = categories.filter(id=selected_category).first()
        if records:
            # Get Category wise technical aspect
            TECHNICAL_ASPECTS = list(AspectsMetaData.objects.filter(my_roga_category=selected_category) \
                .values_list('name', flat=True))
    else:
        records = products
        selected_category = ""
    
    if selected_product:
        records = records.filter(id=selected_product)
        selected_product = products.filter(id=selected_product).first()
        # Get Selected Product Technical aspect
        product_technical_aspects = list(selected_product.technical_aspects.values_list('name', flat=True))

        # Get only those technical aspect which is common in Category wise & selected Product.
        if selected_category:
            TECHNICAL_ASPECTS = list(set(TECHNICAL_ASPECTS).intersection(product_technical_aspects))
        else:
            TECHNICAL_ASPECTS = product_technical_aspects
    else:
        selected_product = ""

    results = []
    for record in records:
        result = {}
        result['Product ID'] = record.id
        result['Category'] = record.my_roga_category.name
        result['Product Status'] = record.get_product_status_display()
        result['Product Stealth'] = record.product_stealth
        result['Language'] = record.language.name if record.language else ''
        result['Image URL'] = record.image_url if record.image_url else ''
        result['Review URL'] = record.review_url if record.review_url else ''
        result['Review Count'] = record.review_count
        result['Review Score'] = record.review_score
        result['Hero Offer Url'] = record.hero_offer_url
        result['Hero Offer Price'] = record.hero_offer_price
        result['Hero Offer Marketplace ID'] = record.hero_offer_market_place.id if record.hero_offer_market_place else ''
        result['Second Offer Url'] = record.second_hero_offer_url
        result['Second Offer Price'] = record.second_hero_offer_price
        result['Second Offer Marketplace ID'] = record.second_hero_offer_market_place.id if record.second_hero_offer_market_place else ''
        result['Updated At'] = record.updated_at

        for aspect in TECHNICAL_ASPECTS:
            aspect_obj = AspectsMetaData.objects.filter(name=aspect).first()
            if aspect_obj:
                aspect_value = record.technical_aspect_values.filter(aspect_meta_data=aspect_obj).first()
                if aspect_value:
                    result[aspect] = aspect_value.value_name
                else:
                    result[aspect] = ''
            else:
                result[aspect] = ''

        results.append(result)

    DEFAULT_COLUMNS += TECHNICAL_ASPECTS + ['Updated At']
    COLUMNS = DEFAULT_COLUMNS

    return {
        "COLUMNS": COLUMNS,
        "results": results,
        "selected_category": selected_category,
        "selected_product": selected_product
    }


def get_model_catalog_formatted_products(products, category):
    DEFAULT_COLUMNS = copy.deepcopy(PRODUCT_DEFAULT_COLUMNS)
    # Get Category wise technical aspect & must be is Model aspect
    TECHNICAL_ASPECTS = list(AspectsMetaData.objects.filter(my_roga_category=category, is_model_aspect=True) \
        .values_list('name', flat=True))

    results = []
    records = products
    for record in records:
        result = {}
        result['Product ID'] = record.id
        result['Category'] = record.my_roga_category.name
        result['Product Status'] = record.get_product_status_display()
        result['Product Stealth'] = record.product_stealth
        result['Language'] = record.language.name if record.language else ''
        result['Image URL'] = record.image_url if record.image_url else ''
        result['Review URL'] = record.review_url if record.review_url else ''
        result['Review Count'] = record.review_count
        result['Review Score'] = record.review_score
        result['Hero Offer Url'] = record.hero_offer_url
        result['Hero Offer Price'] = record.hero_offer_price
        result['Hero Offer Marketplace ID'] = record.hero_offer_market_place.name if record.hero_offer_market_place else ''
        result['Second Offer Url'] = record.second_hero_offer_url
        result['Second Offer Price'] = record.second_hero_offer_price
        result['Second Offer Marketplace ID'] = record.second_hero_offer_market_place.name if record.second_hero_offer_market_place else ''
        result['Updated At'] = record.updated_at

        for aspect in TECHNICAL_ASPECTS:
            aspect_obj = AspectsMetaData.objects.filter(name=aspect).first()
            if aspect_obj:
                aspect_value = record.technical_aspect_values.filter(aspect_meta_data=aspect_obj).first()
                if aspect_value:
                    result[aspect] = aspect_value.value_name
                else:
                    result[aspect] = ''
            else:
                result[aspect] = ''

        results.append(result)

    DEFAULT_COLUMNS += TECHNICAL_ASPECTS + ['Updated At']
    COLUMNS = DEFAULT_COLUMNS
    return {
        "COLUMNS": COLUMNS,
        "results": results,
    }