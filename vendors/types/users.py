
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.users import Users as UserModel


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)
