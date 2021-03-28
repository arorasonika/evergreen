
import graphene

from ..schema.query import Query

from ..types.vendors import Vendors
from ..types.users import Users

schema = graphene.Schema(query=Query, types=[Vendors, Users])
