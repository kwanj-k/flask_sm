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

class CreateProduct(graphene.Mutation):
    """
        Returns the product payload after creating
    """
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Int(required=True)
        category = graphene.String(required=True)
    product = graphene.Field(ProductObject)

    def mutate(self, info, **kwargs):
        product = Product(**kwargs)
        product.save()
        return CreateProduct(product=product)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field(
        description="Creates a new product with the arguments")
