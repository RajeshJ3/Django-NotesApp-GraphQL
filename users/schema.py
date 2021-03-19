from django.contrib import auth
import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    obtain_token = mutations.ObtainJSONWebToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    update_account = mutations.UpdateAccount.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
