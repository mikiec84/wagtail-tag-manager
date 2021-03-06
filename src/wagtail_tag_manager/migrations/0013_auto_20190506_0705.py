# Generated by Django 2.1.8 on 2019-05-06 07:05

import modelcluster.fields
import django.db.models.deletion
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tag_manager', '0012_auto_20190501_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='TriggerCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('variable', models.CharField(max_length=255, null=True)),
                ('condition_type', models.CharField(choices=[('Text', (('exact_match', 'exact match'), ('not_exact_match', 'not exact match'), ('contains', 'contains'), ('not_contains', 'does not contain'), ('starts_with', 'starts with'), ('not_starts_with', 'does not start with'), ('ends_with', 'ends with'), ('not_ends_with', 'does not end with'))), ('Regex', (('regex_match', 'matches regex'), ('not_regex_match', 'does not match regex'), ('regex_imatch', 'matches regex (case insensitive)'), ('not_regex_imatch', 'does not match regex (case insensitive)'))), ('Numbers', (('lower_than', 'is lower than'), ('lower_than_equal', 'is lower than or equal to'), ('greater_than', 'is greater than'), ('greater_than_equal', 'is greater than or equal to')))], default='contains', max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='trigger',
            name='active',
            field=models.BooleanField(default=True, help_text='Uncheck to disable this trigger from firing.'),
        ),
        migrations.AddField(
            model_name='trigger',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trigger',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trigger',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trigger',
            name='tags',
            field=models.ManyToManyField(help_text='The tags to include when this trigger is fired.', to='wagtail_tag_manager.Tag'),
        ),
        migrations.AddField(
            model_name='trigger',
            name='trigger_type',
            field=models.CharField(choices=[('form_submit', 'Form submit'), ('history_change', 'History change'), ('javascript_error', 'JavaScript error'), ('Click', (('click_all_elements', 'Click on all elements'), ('click_some_elements+', 'Click on some elements'))), ('Visibility', (('visibility_once_per_page+', 'Monitor once per page'), ('visibility_once_per_element+', 'Monitor once per element'), ('visibility_recurring+', 'Monitor recurringingly'))), ('Scroll', (('scroll_vertical+', 'Scroll vertical'), ('scroll_horizontal+', 'Scroll horizontal'))), ('Timer', (('timer_timeout+', 'Timer with timeout'), ('timer_interval+', 'Timer with interval')))], default='form_submit', max_length=255),
        ),
        migrations.AddField(
            model_name='trigger',
            name='value',
            field=models.CharField(blank=True, help_text='<b>Click:</b> the query selector of the element(s).<br/><b>Visibility:</b> the query selector of the element(s).<br/><b>Scroll:</b> the distance after which to trigger as percentage.<br/><b>Timer:</b> the time in milliseconds after which to trigger.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='triggercondition',
            name='trigger',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='wagtail_tag_manager.Trigger'),
        ),
    ]
