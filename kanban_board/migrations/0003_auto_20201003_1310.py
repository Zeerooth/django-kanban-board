# Generated by Django 3.1.1 on 2020-10-03 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_board', '0002_auto_20200918_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanbanboardelement',
            name='kanban_board_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kanban_board.kanbanboard'),
        ),
    ]
