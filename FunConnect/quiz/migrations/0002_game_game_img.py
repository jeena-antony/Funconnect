# Generated by Django 3.2.6 on 2021-10-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_img',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.food4fuel.com%2Fproduct%2F21-day-stc-option-1%2F&psig=AOvVaw1P7wa_V1NqQlM-XoYwlszW&ust=1633366451217000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLj06q3arvMCFQAAAAAdAAAAABAD', max_length=500),
        ),
    ]
