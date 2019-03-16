import graphene
import api.product.schema

class Query(api.product.schema.Query):
    pass

schema = graphene.Schema(query=Query)

