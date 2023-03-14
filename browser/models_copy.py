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

