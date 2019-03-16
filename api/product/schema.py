import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func

from .models import Product

class ProductObject(SQLAlchemyObjectType):
    class Meta:
        model = Product

class Query(graphene.ObjectType):
    all_products = graphene.List(
        ProductObject,
        description="Query That returns a list of all products")

    def resolve_all_products(self, info):
        """
            Returns list of all products
        """
        query = ProductObject.get_query(info)
        return query.order_by(func.lower(Product.name)).all()
