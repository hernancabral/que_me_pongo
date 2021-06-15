from django.db.models.fields.related_descriptors import ReverseOneToOneDescriptor
from django.db.models import OneToOneField

"""
STOLEN FROM NICO
In the normal OneToOne (e.g. Profile --> User), if you try the reverse relation (`user.profile`) when there is no object you got an error.
With this, you got None instead of Error.
"""


class CustomReverseOneToOneDescriptor(ReverseOneToOneDescriptor):
    def __get__(self, instance, cls=None):
        try:
            return super().__get__(instance, cls)
        except self.RelatedObjectDoesNotExist:
            return None

class OneToOneField(OneToOneField):
    """Like models.OneToOneField, but the reverse relation works fine."""
    related_accessor_class = CustomReverseOneToOneDescriptor