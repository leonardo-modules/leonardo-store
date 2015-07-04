
from import_export import resources

from oscar.core.loading import get_model

UserAdress = get_model('address', 'UserAddress')


class UserAddressResource(resources.ModelResource):

    class Meta:
        model = UserAdress
        fields = ('id', 'title', 'first_name', 'last_name', 'user__email',
                  'line1', 'line2', 'line3', 'state', 'city', 'postcode',
                  'country', 'phone_number', 'notes', )
