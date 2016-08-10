from operator import __or__ as OR
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.db.models import Q
from django.utils.encoding import force_unicode
from birth_registration.codes import CODES, label_from_tuple
from django.conf import settings


def create_location_related_permissions(content_type, do_create_permissions=False, delete_existing_permissions=False):
    def create_permission(codename, name):
        permissions[codename] = name
        if do_create_permissions:

            permission = Permission.objects.filter(codename=codename)

            if permission.exists() and delete_existing_permissions:
                if settings.DEBUG:
                    print "Permission exists %s - %s deleting" % (codename, name)
                permission.delete()

            if not permission.exists():
                Permission.objects.create(
                    codename=codename,
                    name=name,
                    content_type=content_type
                )
                if settings.DEBUG:
                    print "Permission created: %s - %s" % (codename, name)
            else:
                if settings.DEBUG:
                    if not str(permission.first().codename) == str(codename):
                        print "Codename - wrong, should be (%s) not (%s)" % (permission.first().codename, codename)
                    if not permission.first().name == name:
                        print "Name - wrong, should be (%s) not (%s)" % (permission.first().name, name)

    permissions = {}

    for state_divisions in CODES:

        state_division_codename, state_division_name = state_divisions[0]
        state_division_label = label_from_tuple(state_divisions[0])

        permissions[state_division_codename] = state_division_label
        create_permission(state_division_codename, state_division_label)

        for districts in state_divisions[1]:

            district_code, district_name = districts[0]
            district_codename = get_codename([state_division_codename, district_code])
            district_label = u"%s - %s/%s" % (district_codename, state_division_name, district_name)

            create_permission(district_codename, district_label)

            for township_or_town in districts[1]:
                township_or_town_code, township_or_town_number, township_or_town_name = township_or_town[:3]

                township_or_town_codename = get_codename([state_division_codename, district_code,
                                                          township_or_town_code])
                township_or_town_label = u"%02d/%02d/%02d - %s/%s/%s" % (state_division_codename, district_code,
                                                                         township_or_town_number, state_division_name,
                                                                         district_name, township_or_town_name)

                create_permission(township_or_town_codename, township_or_town_label)

    if settings.DEBUG:
        print "Total of %d permissions" % len(permissions)

    return permissions


def get_codename(codes):
    if len(codes) == 3:
        return "%02d/%02d/%03d" % (codes[0], codes[1], codes[2])

    if len(codes) == 2:
        return "%02d/%02d" % (codes[0], codes[1])

    return codes[0]



def _add_location(new, olds):
    news = []

    for old in olds:
        if all(i == k for i, k in zip(new, old)):
            if old < new:
                return olds
        else:
            news.append(old)
    return news + [new]


def _check_location(user_locations, location):
    for user_location in user_locations:
        if all(i == k for i, k in zip(location, user_location)):
            if user_location < location:
                return True
    return False


def check_location(user, location):
    return _check_location(get_user_locations(user), location)


def get_user_locations(user):
    permissions = user.get_all_permissions()

    locations = []
    for permission in permissions:
        app, location = permission.split(".")
        if app == 'birth_registration':
            n = location.split("/")
            if n[0].isdigit():
                n = map(int, n)
                locations = _add_location(n, locations)
    return sorted(locations)


def get_user_location_names(user):
    permissions = create_location_related_permissions(
        ContentType.objects.get(app_label="birth_registration", model="f101")
    )

    location_names = []
    for location in get_user_locations(user):
        location_names.append(
            force_unicode(permissions[get_codename(location)])
        )

    return location_names


def get_user_Q_s(user, form_name, q=None):
    if not q:
        q = []
    for location in get_user_locations(user):
        if form_name in ("f101", "f103"):
            fields = dict(zip(['ST_DV', 'DIS', 'TWN'], location))
        elif form_name in ("f201", "f203"):
            fields = dict(zip(['NNRT', 'NNRT1', 'NNST'], location))
        else:
            raise NotImplementedError("Location fields are not defined for form %s" % form_name)

        q.append(Q(**fields))

    if q:
        q = reduce(OR, q)

    return q
