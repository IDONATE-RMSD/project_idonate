from django.contrib import admin

from .models import Signupp
from .models import Detail
from .models import Detail2
from .models import Rdetail2
from .models import Rdetail
from .models import Odetail
from .models import Odetail2
from .models import Hdetail
from .models import Hdetail2
from .models import Quick
from .models import Edit
from .models import Recreq
from .models import Donreq
from .models import Orgreq
from .models import Hosreq


# Register your models here.

admin.site.register(Signupp)
admin.site.register(Detail)
admin.site.register(Detail2)
admin.site.register(Rdetail2)
admin.site.register(Rdetail)
admin.site.register(Odetail)
admin.site.register(Odetail2)
admin.site.register(Hdetail)
admin.site.register(Hdetail2)
admin.site.register(Quick)
admin.site.register(Edit)
admin.site.register(Recreq)
admin.site.register(Donreq)
admin.site.register(Orgreq)
admin.site.register(Hosreq)