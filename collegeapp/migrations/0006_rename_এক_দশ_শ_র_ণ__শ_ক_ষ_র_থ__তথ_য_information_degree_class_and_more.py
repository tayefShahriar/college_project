# Generated by Django 4.2.5 on 2023-10-04 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0005_information_rename_pdf_notice_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='একাদশ_শ্রেণি_শিক্ষার্থী_তথ্য',
            new_name='degree_class',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='এমপিও_তথ্য',
            new_name='eleven_class',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='ডিগ্রি_শিক্ষার্থী_তথ্য',
            new_name='managing_committee',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='দ্বাদশ_শ্রেণি_শিক্ষার্থী_তথ্য',
            new_name='mpo_info',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='পাঠদান_সংক্রান্ত',
            new_name='pathdan_songkranto',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='প্রতিষ্ঠান_পরিচিতি',
            new_name='protisthan_porichiti',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='ব্যাবস্থাপনা_কমিটি',
            new_name='teacher_staff',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='শিক্ষক_কর্মচারী',
            new_name='tweleve_class',
        ),
    ]
