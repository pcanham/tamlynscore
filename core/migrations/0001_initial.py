# -*- coding: utf-8 -*-

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, db_index=True, verbose_name='email address', max_length=255)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', verbose_name='groups', blank=True)),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
        ),
        migrations.CreateModel(
            name='Archer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1, choices=[(b'G', b'Gent'), (b'L', b'Lady')])),
                ('age', models.CharField(default=b'S', max_length=1, choices=[(b'J', b'Junior'), (b'S', b'Senior')])),
                ('novice', models.CharField(default=b'E', max_length=1, choices=[(b'N', b'Novice'), (b'E', b'Experienced')])),
                ('gnas_no', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bowstyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=500)),
                ('short_name', models.CharField(unique=True, max_length=50)),
                ('abbreviation', models.CharField(default=b'', max_length=10, blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ('short_name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('country', models.ForeignKey(to='core.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('scoring_type', models.CharField(max_length=1, choices=[(b'F', b'Five Zone Imperial'), (b'T', b'AGB Indoor - Ten Zone, no Xs, with hits'), (b'X', b'WA Outdoor - Ten Zone, with Xs, no hits'), (b'I', b'WA Indoor - Ten Zone, no Xs, no hits'), (b'W', b'Worcester')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subround',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrows', models.PositiveIntegerField()),
                ('distance', models.PositiveIntegerField()),
                ('unit', models.CharField(max_length=1, choices=[(b'm', b'metres'), (b'y', b'yards')])),
                ('target_face', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('unit', '-distance', '-arrows', '-target_face'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='round',
            name='subrounds',
            field=models.ManyToManyField(to='core.Subround'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='county',
            name='region',
            field=models.ForeignKey(to='core.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='club',
            name='county',
            field=models.ForeignKey(blank=True, to='core.County', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archer',
            name='bowstyle',
            field=models.ForeignKey(to='core.Bowstyle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='archer',
            name='club',
            field=models.ForeignKey(to='core.Club'),
            preserve_default=True,
        ),
    ]
