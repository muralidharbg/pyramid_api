from .meta import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime
from sqlalchemy.sql.functions import func

class BrandModel(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=60), nullable=False, unique=True)
    model_count = Column(Integer, default=0)
    create_date = Column(TIMESTAMP, default=func.now())
    last_modified = Column(DateTime, default=func.now())
    
    def __json__(self, request):
        json_exclude = getattr(self, '__json_exclude__', set())
        dict_obj = {key: value for key, value in self.__dict__.items()
                # Do not serialize 'private' attributes
                # (SQLAlchemy-internal attributes are among those, too)
                if not key.startswith('_')
                and key not in json_exclude}
        dict_obj["create_date"] = dict_obj["create_date"].__str__()
        dict_obj["last_modified"] = dict_obj["last_modified"].__str__()
        return dict_obj
    
#     def __init__(self, name):
#         self.name = name