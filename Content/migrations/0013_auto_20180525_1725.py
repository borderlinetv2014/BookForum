# Generated by Django 2.0.5 on 2018-05-25 09:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Content', '0012_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auther',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['pub_date'], 'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name': '滚动图', 'verbose_name_plural': '滚动图'},
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': '投票信息', 'verbose_name_plural': '投票信息'},
        ),
        migrations.AlterModelOptions(
            name='publishing',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '书籍标签', 'verbose_name_plural': '书籍标签'},
        ),
        migrations.AlterField(
            model_name='auther',
            name='about',
            field=models.TextField(blank=True, max_length=1280, verbose_name='关于作者'),
        ),
        migrations.AlterField(
            model_name='auther',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='作者名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='book_cover/default.jpg', upload_to='book_cover/%Y/%m/%d',
                                    verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='book',
            name='intro',
            field=models.TextField(blank=True, max_length=1280, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=32, verbose_name='书籍名称'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='intro',
            field=models.TextField(blank=True, max_length=128, verbose_name='展示介绍'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='name',
            field=models.CharField(blank=True, max_length=32, verbose_name='图片名字'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='down',
            field=models.IntegerField(default=0, verbose_name='反对'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='up',
            field=models.IntegerField(default=0, verbose_name='赞同'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='about',
            field=models.TextField(blank=True, max_length=1024, verbose_name='关于出版社'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='establish_date',
            field=models.DateField(blank=True, null=True, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='出版社名'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='标签名'),
        ),
    ]
