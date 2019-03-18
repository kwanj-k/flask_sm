import graphene
import api.product.schema

class Query(api.product.schema.Query):
    pass

class Mutation(api.product.schema.Mutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
