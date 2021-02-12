from product.models import AspectsMetaData, AspectValuesMetaData


def get_formatted_model_catalogs(records, selected_category_id=None):
    results = []
    TECHNICAL_ASPECTS = []
    for record in records:
        result = {}

        hero_product = ''
        hero_product_price = 0
        hero_product_market_place = ''
        if record.hero_product:
            hero_product = record.hero_product.title if record.hero_product else ''
            hero_product_price = record.hero_product_price if record.hero_product_price else 0
            hero_product_market_place = record.hero_product_market_place.name if record.hero_product_market_place else ''
        
        second_hero_product = ''
        second_hero_product_price = 0
        second_hero_product_market_place = ''
        if record.second_hero_product:
            second_hero_product = record.second_hero_product.title if record.second_hero_product else ''
            second_hero_product_price = record.second_hero_product_price if record.second_hero_product_price else 0
            second_hero_product_market_place = record.second_hero_product_market_place.name if record.second_hero_product_market_place else ''

        result['id'] = record.id
        result['title'] = record.title
        result['my_roga_category'] = record.my_roga_category
        result['aggregation_key'] = record.model_aggregation_key
        result['model_stealth'] = record.model_stealth if record.model_stealth else ''
        result['model_status'] = record.get_model_status_display() if record.model_status else ''
        result['description'] = record.description if record.description else ''
        result['description_image_url'] = record.description_image_url if record.description_image_url else ''
        result['image_url'] = record.image_url if record.image_url else ''
        result['language'] = record.language.name if record.language else ''
        result['hero_product'] = hero_product
        result['hero_product_price'] = hero_product_price
        result['hero_product_market_place'] = hero_product_market_place
        result['second_hero_product'] = second_hero_product
        result['second_hero_product_price'] = second_hero_product_price
        result['second_hero_product_market_place'] = second_hero_product_market_place
        result['review_url'] = record.review_url
        result['product_review_count'] = record.product_review_count
        result['product_review_score'] = record.product_review_score
        result['recommendation_score'] = record.recommendation_score if record.recommendation_score else ''
        result['updated_at'] = record.updated_at

        if selected_category_id:
            TECHNICAL_ASPECTS = list(AspectsMetaData.objects.filter(my_roga_category__id=selected_category_id, \
                is_model_aspect=True).values_list('name', flat=True))
        else:
            TECHNICAL_ASPECTS = list(record.aggregation_model_set.aspects.filter(my_roga_category=record.my_roga_category, \
                is_model_aspect=True).values_list('name', flat=True))

        product = record.product_catalog.all()[0]
        for aspect in TECHNICAL_ASPECTS:
            aspect_obj = AspectsMetaData.objects.filter(name=aspect).first()
            if aspect_obj:
                aspect_value =  product.technical_aspect_values.filter(aspect_meta_data=aspect_obj).first()
                if aspect_value:
                    result[aspect] = aspect_value.value_name
                else:
                    result[aspect] = ''
            else:
                result[aspect] = ''
        results.append(result)
    return {
        'COLUMNS': TECHNICAL_ASPECTS,
        'results': results,
    }
