
import graphene
from graphene import relay

from ..models.vendors import Vendors as VendorModel
from ..models.users import Users as UserModel
from ..types.vendors import Vendors


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    vendors_by_name = graphene.List(Vendors, name=graphene.String())
    vendors_by_status = graphene.List(Vendors, name=graphene.String())
    vendors_by_risk = graphene.List(Vendors, name=graphene.String())
    vendors_by_category = graphene.List(Vendors, name=graphene.String())
    all_vendors = graphene.List(Vendors)

    @staticmethod
    def resolve_vendors_by_name(parent, info, **args):
        q = args.get('name')

        vendors_query = Vendors.get_query(info)

        return vendors_query.filter(VendorModel.name.contains(q)).all()

    @staticmethod
    def resolve_vendors_by_status(parent, info, **args):
        q = args.get('name')

        vendors_query = Vendors.get_query(info)

        return vendors_query.filter(VendorModel.status == q).all()

    @staticmethod
    def resolve_vendors_by_risk(parent, info, **args):
        q = args.get('name')

        vendors_query = Vendors.get_query(info)

        return vendors_query.filter(VendorModel.risk == q).all()

    @staticmethod
    def resolve_vendors_by_category(parent, info, **args):
        q = args.get('name')

        vendors_query = Vendors.get_query(info)

        return vendors_query.filter(VendorModel.category == q).all()

    @staticmethod
    def resolve_all_vendors(parent, info):

        vendors_query = Vendors.get_query(info)

        return vendors_query.all()
