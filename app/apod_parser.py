def parse_apod_response(data):
    if isinstance(data, list):
        return [parse_single_apod(item) for item in data]
    else:
        return parse_single_apod(data)

def parse_single_apod(item):
    return {
        'resource': item.get('resource'),
        'concept_tags': item.get('concept_tags'),
        'title': item.get('title'),
        'date': item.get('date'),
        'url': item.get('url'),
        'hdurl': item.get('hdurl'),
        'media_type': item.get('media_type'),
        'explanation': item.get('explanation'),
        'concepts': item.get('concepts'),
        'thumbnail_url': item.get('thumbnail_url'),
        'copyright': item.get('copyright'),
        'service_version': item.get('service_version')
    }