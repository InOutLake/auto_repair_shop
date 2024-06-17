# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Box(models.Model):
    box_number = models.SmallIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Box'


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, blank=True, null=True)
    model_name = models.ForeignKey('Model', models.DO_NOTHING, db_column='model_name')
    number = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'Car'


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    second_name = models.TextField()
    telephone_number = models.TextField()

    class Meta:
        managed = False
        db_table = 'Client'


class Master(models.Model):
    snils = models.TextField(primary_key=True)
    name = models.TextField()
    second_name = models.TextField()
    telephone_number = models.TextField()

    class Meta:
        managed = False
        db_table = 'Master'


class MasterTask(models.Model):
    snils = models.OneToOneField(Master, models.DO_NOTHING, db_column='snils', primary_key=True)  # The composite primary key (snils, id) found, that is not supported. The first column is selected.
    id = models.ForeignKey('Task', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'Master_task'
        unique_together = (('snils', 'id'),)


class Material(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Material'


class MaterialsForTask(models.Model):
    material = models.OneToOneField(Material, models.DO_NOTHING, primary_key=True)  # The composite primary key (material_id, task_type_id) found, that is not supported. The first column is selected.
    quantity = models.IntegerField()
    task_type = models.ForeignKey('TaskType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Materials_for_task'
        unique_together = (('material', 'task_type'),)


class Model(models.Model):
    name = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Model'


class SubtasksInTask(models.Model):
    task = models.OneToOneField('Task', models.DO_NOTHING, primary_key=True)  # The composite primary key (task_id, task_type_id) found, that is not supported. The first column is selected.
    task_type = models.ForeignKey('TaskType', models.DO_NOTHING)
    quantity = models.IntegerField()
    coef = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Subtasks_in_task'
        unique_together = (('task', 'task_type'),)


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    car = models.ForeignKey(Car, models.DO_NOTHING, blank=True, null=True)
    box_number = models.ForeignKey(Box, models.DO_NOTHING, db_column='box_number')
    startdatetime = models.DateTimeField(db_column='StartDateTime')  # Field name made lowercase.
    plannedenddatetime = models.DateTimeField(db_column='PlannedEndDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Task'


class TaskType(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_name = models.ForeignKey(Model, models.DO_NOTHING, db_column='model_name')
    name = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Task_type'
