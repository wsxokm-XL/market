class KeyWords(models.Model):
    shops = models.OneToOneField('Shops', models.DO_NOTHING, primary_key=True)
    key_word = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'key_words'
        unique_together = (('shops', 'key_word'),)


class ShoppingRecords(models.Model):
    shopping_id = models.AutoField(primary_key=True)
    id = models.ForeignKey('Users', models.DO_NOTHING, db_column='id')
    shops = models.ForeignKey('Shops', models.DO_NOTHING)
    nums = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_records'

class Shops(models.Model):
    shops_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    stock = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shops'