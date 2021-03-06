# Generated by Django 3.2 on 2021-12-21 14:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.ImageField(blank=True, null=True, upload_to='Pin/Pic/')),
                ('heading', models.TextField(max_length=100)),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('details', models.TextField(blank=True, max_length=1000, null=True)),
                ('owner', models.PositiveIntegerField(blank=True, null=True)),
                ('pincategory', models.CharField(choices=[('Campus', 'Campus'), ('Carrer', 'Carrer'), ('Culture', 'Culture'), ('Sports', 'Sports'), ('Student', 'Student'), ('Teacher', 'Teacher')], default='Campus', max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('postedtime', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dept', models.CharField(choices=[('', 'Depertment'), ('Not Applicable', 'Not Applicable'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil '), ('Electrical', 'Electrical'), ('ComputerScience', 'Computer Science'), ('Electronics&Communication', 'Electronics & Communication')], default='Computer Science', max_length=40)),
                ('year', models.CharField(choices=[('', 'Year'), ('Not Applicable', 'Not Applicable'), ('FirstYear', 'First Year'), ('SecondYear', 'Second Year '), ('ThirdYear', 'Third Year'), ('FourthYear', 'Fourth Year')], default='First Year', max_length=40)),
                ('semester', models.CharField(choices=[('', 'Semester'), ('Not Applicable', 'Not Applicable'), ('FirstSemester', 'First Semester'), ('SecondSemester', 'Second Semester '), ('ThirdSemester', 'Third Semester'), ('FourthSemester', 'Fourth Semester'), ('FifthSemester', 'Fifth Semester'), ('SixthSemester', 'Sixth Semester'), ('SeventhSemester', 'Seventh Semester'), ('EightthSemester', 'Eightth Semester')], default='First Semester', max_length=40)),
                ('enrollment', models.CharField(blank=True, max_length=70, null=True)),
                ('profilepic', models.ImageField(blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1633459954/usericon_hpewnq.png', null=True, upload_to='profile_pic/')),
                ('is_cdc', models.BooleanField(default=False, verbose_name='Is cdc')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Is teacher')),
                ('is_student', models.BooleanField(default=False, verbose_name='Is student')),
                ('status', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
