# from pyramid_api.views.brands_view import BrandsView

def includeme(config):
#     config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('brands', '/brands')
    config.add_route('brands_id', '/brands/{id}')
#     config.add_route('brands', '/brands/get')
#     config.add_view(BrandsView, attr='get', request_method='GET')
