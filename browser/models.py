# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


"""
data starts:
"""


class Titlebasics(models.Model):
    tconst = models.CharField(max_length=100, primary_key=True)
    titletype = models.CharField(max_length=100,
                                 db_column='titleType',
                                 blank=True, null=True)
    primarytitle = models.CharField(max_length=100,
                                    db_column='primaryTitle',
                                    blank=True, null=True)
    originaltitle = models.CharField(max_length=100,
                                     db_column='originalTitle',
                                     blank=True, null=True)
    isadult = models.CharField(
        max_length=100, db_column='isAdult', blank=True, null=True)
    startyear = models.CharField(
        max_length=100, db_column='startYear', blank=True, null=True)
    endyear = models.CharField(
        max_length=100, db_column='endYear', blank=True, null=True)
    runtimeminutes = models.CharField(max_length=100,
                                      db_column='runtimeMinutes', blank=True, null=True)
    genres = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titlebasics'


class Namebasics(models.Model):
    nconst = models.CharField(max_length=100, primary_key=True)
    primaryname = models.CharField(max_length=128,
                                   db_column='primaryName',
                                   blank=True, null=True)
    birthyear = models.CharField(max_length=128,
                                 db_column='birthYear',
                                 blank=True, null=True)
    deathyear = models.CharField(max_length=128,
                                 db_column='deathYear',
                                 blank=True, null=True)
    primaryprofession = models.CharField(max_length=128,
                                         db_column='primaryProfession',
                                         blank=True, null=True)
    knownfortitles = models.CharField(max_length=128,
                                      db_column='knownForTitles',
                                      blank=True, null=True)

    def __str__(self):
        return self.primaryname

    class Meta:
        managed = False
        db_table = 'namebasics'


class Titleakas(models.Model):
    titleid = models.TextField(db_column='titleId', blank=True, null=True)
    ordering = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    types = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    isoriginaltitle = models.TextField(
        db_column='isOriginalTitle', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titleakas'


class Titlecrew(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    tconst = models.TextField(blank=True, null=True)
    directors = models.TextField(blank=True, null=True)
    writers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titlecrew'


class Titleepisode(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    tconst = models.TextField(blank=True, null=True)
    parenttconst = models.TextField(
        db_column='parentTconst', blank=True, null=True)
    seasonnumber = models.TextField(
        db_column='seasonNumber', blank=True, null=True)
    episodenumber = models.TextField(
        db_column='episodeNumber', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titleepisode'


class Titleprincipals(models.Model):
    tconst = models.TextField(blank=True, null=True)
    ordering = models.TextField(blank=True, null=True)
    nconst = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titleprincipals'


class Titleratings(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    tconst = models.TextField(blank=True, null=True)
    averagerating = models.FloatField(
        db_column='averageRating', blank=True, null=True)
    numvotes = models.BigIntegerField(
        db_column='numVotes', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titleratings'


"""
Define some new fields 
"""


class TextBooleanField(models.CharField):
    description = _("1" is True, "0" is False)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 1)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return value == '1'

    def to_python(self, value):
        if isinstance(value, bool):
            return bool
        if value is None:
            return None
        return value == '1'

    def get_prep_value(self, value):
        if value is None:
            return None
        return '1' if value else '0'
