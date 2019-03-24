import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func

from .models import Product as ProductModel
from utilities.utility import update_entity_fields

class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel

class Query(graphene.ObjectType):
    all_products = graphene.List(
        Product,
        description="Query That returns a list of all products")

    def resolve_all_products(self, info):
        """
            Returns list of all products
        """
        query = Product.get_query(info)
        return query.order_by(func.lower(ProductModel.name)).all()

class CreateProduct(graphene.Mutation):
    """
        Returns the product payload after creating
    """
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Int(required=True)
        category = graphene.String(required=True)
    product = graphene.Field(Product)

    def mutate(self, info, **kwargs):
        product = ProductModel(**kwargs)
        product.save()
        return CreateProduct(product=product)

class UpdateProduct(graphene.Mutation):

    class Arguments:
        name = graphene.String()
        price = graphene.Int()
        category = graphene.String()
        product_id = graphene.Int()
    product = graphene.Field(Product)

    def mutate(self, info, product_id, **kwargs):
        product = Product.get_query(info)
        product_obj = product.filter(
            ProductModel.id == product_id
        ).first()
        if not product:
            raise GraphQLError("ProductModel not found")
        update_entity_fields(product_obj, **kwargs)
        product_obj.save()
        return UpdateProduct(product=product_obj)

class DeleteProduct(graphene.Mutation):
    """
        Returns the product payload after deleting a product
    """
    class Arguments:
        product_id = graphene.Int(required=True)

    product = graphene.Field(Product)

    def mutate(self, info, product_id, **kwargs):
        query = Product.get_query(info)
        product = query.filter(ProductModel.id == product_id).first()
        if not product:
            raise GraphQLError("ProductModel not found")
        product.delete()
        return DeleteProduct(product=product)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field(
        description="Creates a new product with the arguments")
    update_product = UpdateProduct.Field(
        description="Updates existing product"
    )
    delete_product =  DeleteProduct.Field(
        description = "Delete product"
    )
