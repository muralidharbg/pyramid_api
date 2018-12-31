from pyramid.view import view_defaults, view_config
from pyramid.response import Response
from pyramid_api.models.brand_model import BrandModel
from sqlalchemy.exc import DBAPIError
from sqlalchemy import desc



@view_defaults(route_name='brands')
class BrandsView:
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', renderer='json')
    def get(self):
        try:
            query = self.request.dbsession.query(BrandModel)
            all_brands = query.order_by(desc(BrandModel.create_date)).all()
            print(all_brands)
            print(type(all_brands))
        except DBAPIError:
            return Response("error", content_type='text/plain', status=500)
        
        return all_brands
    
    @view_config(request_method='POST', renderer='json')
    def post(self):
#         print(self.request.json_body['name'])
        new_brand = BrandModel()
        new_brand.name = self.request.json_body['name']
        
        dbsession = self.request.dbsession
        dbsession.add(new_brand)
        
        return Response()
    
    @view_config(request_method='PUT', renderer='json', route_name='brands_id')
    def put(self):
        brand_id = self.request.matchdict['id']
        try:
            query = self.request.dbsession.query(BrandModel)
            brand = query.filter(BrandModel.id == brand_id).order_by(desc(BrandModel.create_date)).one()
            
            for key, value in self.request.json_body.items():
                print(key, value)
                if hasattr(brand, key):
                    setattr(brand, key, value)
            
        except DBAPIError:
            return Response("error", content_type='text/plain', status=500)
        
        return brand
    
    @view_config(request_method='GET', renderer='json', route_name='brands_id')
    def get_id(self):
        brand_id = self.request.matchdict['id']
        try:
            query = self.request.dbsession.query(BrandModel)
            brand = query.filter(BrandModel.id == brand_id).order_by(desc(BrandModel.create_date)).one()
            
        except DBAPIError:
            return Response("error", content_type='text/plain', status=500)
        
        return brand
    
    @view_config(request_method='DELETE', renderer='json', route_name='brands_id')
    def delete_id(self):
        brand_id = self.request.matchdict['id']
        try:
            query = self.request.dbsession.query(BrandModel)
            brand = query.filter(BrandModel.id == brand_id).order_by(desc(BrandModel.create_date)).one()
            self.request.dbsession.delete(brand)
            
        except DBAPIError:
            return Response("error", content_type='text/plain', status=500)
        
        return Response()
    