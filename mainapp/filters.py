from .models import Organization
import django_filters

class OrgFilter(django_filters.FilterSet):
	class Meta:
		model = Organization
		fields = {'name', 'bio'}
		