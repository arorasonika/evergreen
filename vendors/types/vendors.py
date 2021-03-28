
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.vendors import Vendors as VendorModel


class Vendors(SQLAlchemyObjectType):
    class Meta:
        model = VendorModel
        interfaces = (graphene.relay.Node,)


class VendorAttribute:
    name = graphene.String()
    description = graphene.String()
    external_link = graphene.String()
    category = graphene.String()
    status = graphene.String()
    risk = graphene.String()
    tier = graphene.String()

class CreateVendorInput(graphene.InputObjectType, VendorAttribute):
    pass
