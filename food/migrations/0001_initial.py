# Generated by Django 3.2 on 2021-05-25 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('quantity_g', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Ingredient for the Recipe')),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('protein_g', models.FloatField(blank=True, null=True)),
                ('calories', models.FloatField()),
                ('carbohydrate_g', models.FloatField(blank=True, null=True)),
                ('calcium_g', models.FloatField(blank=True, null=True)),
                ('calories_from_fat', models.FloatField(blank=True, null=True)),
                ('total_fat_g', models.FloatField(blank=True, null=True)),
                ('total_fat_dv', models.FloatField(blank=True, null=True)),
                ('sodium_g', models.FloatField(blank=True, null=True)),
                ('sodium_dv', models.FloatField(blank=True, null=True)),
                ('potassium_g', models.FloatField(blank=True, null=True)),
                ('potassium_dv', models.FloatField(blank=True, null=True)),
                ('carbohydrate_dv', models.FloatField(blank=True, null=True)),
                ('dietary_fiber_g', models.FloatField(blank=True, null=True)),
                ('dietary_fiber_dv', models.FloatField(blank=True, null=True)),
                ('sugar_g', models.FloatField(blank=True, null=True)),
                ('Vitamin_A_dv', models.FloatField(blank=True, null=True)),
                ('Vitamin_C_dv', models.FloatField(blank=True, null=True)),
                ('calcium_dv', models.FloatField(blank=True, null=True)),
                ('iron_dv', models.FloatField(blank=True, null=True)),
                ('saturated_fat_dv', models.FloatField(blank=True, null=True)),
                ('saturated_fat_mg', models.FloatField(blank=True, null=True)),
                ('cholesterol_dv', models.FloatField(blank=True, null=True)),
                ('cholesterol_mg', models.FloatField(blank=True, null=True)),
                ('Food_Code', models.CharField(blank=True, max_length=200, null=True)),
                ('Total_solids', models.CharField(blank=True, max_length=20, null=True)),
                ('Nitrogen_conversion_factor', models.CharField(blank=True, max_length=50, null=True)),
                ('Glycerol_conversion_factor', models.CharField(blank=True, max_length=50, null=True)),
                ('WATER', models.CharField(blank=True, max_length=50, null=True)),
                ('FAT_g', models.CharField(blank=True, max_length=50, null=True)),
                ('Energy_kj', models.CharField(blank=True, max_length=50, null=True)),
                ('Starch_g', models.CharField(blank=True, max_length=50, null=True)),
                ('OLIGO_g', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTSUG', models.CharField(blank=True, max_length=50, null=True)),
                ('GLUC', models.CharField(blank=True, max_length=50, null=True)),
                ('GALACT', models.CharField(blank=True, max_length=50, null=True)),
                ('FRUCT', models.CharField(blank=True, max_length=50, null=True)),
                ('SUCR', models.CharField(blank=True, max_length=50, null=True)),
                ('MALT', models.CharField(blank=True, max_length=50, null=True)),
                ('LACT', models.CharField(blank=True, max_length=50, null=True)),
                ('ALCO', models.CharField(blank=True, max_length=50, null=True)),
                ('ENGFIB', models.CharField(blank=True, max_length=50, null=True)),
                ('AOACFIB', models.CharField(blank=True, max_length=50, null=True)),
                ('SATFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTn6PFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTn3PFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('MONOFODc', models.CharField(blank=True, max_length=50, null=True)),
                ('MONOFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('POLYFODc', models.CharField(blank=True, max_length=50, null=True)),
                ('POLYFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('SATFODx6', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTBRFOD_g', models.CharField(blank=True, max_length=50, null=True)),
                ('FODTRANS_g', models.CharField(blank=True, max_length=50, null=True)),
                ('CHOL_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('K_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('CA_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('MG_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('P_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('FE_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('CU_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('ZN_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('CL_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('MN', models.CharField(blank=True, max_length=50, null=True)),
                ('SE', models.CharField(blank=True, max_length=50, null=True)),
                ('I_mug', models.CharField(blank=True, max_length=50, null=True)),
                ('RET', models.CharField(blank=True, max_length=50, null=True)),
                ('CAREQU', models.CharField(blank=True, max_length=50, null=True)),
                ('RETEQU', models.CharField(blank=True, max_length=50, null=True)),
                ('VITD', models.CharField(blank=True, max_length=50, null=True)),
                ('VITE', models.CharField(blank=True, max_length=50, null=True)),
                ('VITK1', models.CharField(blank=True, max_length=50, null=True)),
                ('THIA', models.CharField(blank=True, max_length=50, null=True)),
                ('RIBO', models.CharField(blank=True, max_length=50, null=True)),
                ('NIAC', models.CharField(blank=True, max_length=50, null=True)),
                ('TRYP60', models.CharField(blank=True, max_length=50, null=True)),
                ('NIACEQU', models.CharField(blank=True, max_length=50, null=True)),
                ('VITB6', models.CharField(blank=True, max_length=50, null=True)),
                ('VITB12', models.CharField(blank=True, max_length=50, null=True)),
                ('FOLT', models.CharField(blank=True, max_length=50, null=True)),
                ('PANTO', models.CharField(blank=True, max_length=50, null=True)),
                ('BIOT', models.CharField(blank=True, max_length=50, null=True)),
                ('VITC', models.CharField(blank=True, max_length=50, null=True)),
                ('ALTRET', models.CharField(blank=True, max_length=50, null=True)),
                ('CISRET_13', models.CharField(blank=True, max_length=50, null=True)),
                ('DEHYRET', models.CharField(blank=True, max_length=50, null=True)),
                ('RETALD', models.CharField(blank=True, max_length=50, null=True)),
                ('ACAR', models.CharField(blank=True, max_length=50, null=True)),
                ('BCAR', models.CharField(blank=True, max_length=50, null=True)),
                ('CRYPT', models.CharField(blank=True, max_length=50, null=True)),
                ('LUT', models.CharField(blank=True, max_length=50, null=True)),
                ('LYCO', models.CharField(blank=True, max_length=50, null=True)),
                ('OHD3_25', models.CharField(blank=True, max_length=50, null=True)),
                ('VITD3', models.CharField(blank=True, max_length=50, null=True)),
                ('METHF_5', models.CharField(blank=True, max_length=50, null=True)),
                ('ATOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('BTOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('DTOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('GTOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('ATOTR', models.CharField(blank=True, max_length=50, null=True)),
                ('GTOTR', models.CharField(blank=True, max_length=50, null=True)),
                ('Total_PHYTO', models.CharField(blank=True, max_length=50, null=True)),
                ('PHYTO', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientAlias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Ingredient Alias name')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_g', models.FloatField(blank=True, null=True)),
                ('calories', models.FloatField()),
                ('carbohydrate_g', models.FloatField(blank=True, null=True)),
                ('calcium_g', models.FloatField(blank=True, null=True)),
                ('calories_from_fat', models.FloatField(blank=True, null=True)),
                ('total_fat_g', models.FloatField(blank=True, null=True)),
                ('total_fat_dv', models.FloatField(blank=True, null=True)),
                ('sodium_g', models.FloatField(blank=True, null=True)),
                ('sodium_dv', models.FloatField(blank=True, null=True)),
                ('potassium_g', models.FloatField(blank=True, null=True)),
                ('potassium_dv', models.FloatField(blank=True, null=True)),
                ('carbohydrate_dv', models.FloatField(blank=True, null=True)),
                ('dietary_fiber_g', models.FloatField(blank=True, null=True)),
                ('dietary_fiber_dv', models.FloatField(blank=True, null=True)),
                ('sugar_g', models.FloatField(blank=True, null=True)),
                ('Vitamin_A_dv', models.FloatField(blank=True, null=True)),
                ('Vitamin_C_dv', models.FloatField(blank=True, null=True)),
                ('calcium_dv', models.FloatField(blank=True, null=True)),
                ('iron_dv', models.FloatField(blank=True, null=True)),
                ('saturated_fat_dv', models.FloatField(blank=True, null=True)),
                ('saturated_fat_mg', models.FloatField(blank=True, null=True)),
                ('cholesterol_dv', models.FloatField(blank=True, null=True)),
                ('cholesterol_mg', models.FloatField(blank=True, null=True)),
                ('Food_Code', models.CharField(blank=True, max_length=200, null=True)),
                ('Total_solids', models.CharField(blank=True, max_length=20, null=True)),
                ('Nitrogen_conversion_factor', models.CharField(blank=True, max_length=50, null=True)),
                ('Glycerol_conversion_factor', models.CharField(blank=True, max_length=50, null=True)),
                ('WATER', models.CharField(blank=True, max_length=50, null=True)),
                ('FAT_g', models.CharField(blank=True, max_length=50, null=True)),
                ('Energy_kj', models.CharField(blank=True, max_length=50, null=True)),
                ('Starch_g', models.CharField(blank=True, max_length=50, null=True)),
                ('OLIGO_g', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTSUG', models.CharField(blank=True, max_length=50, null=True)),
                ('GLUC', models.CharField(blank=True, max_length=50, null=True)),
                ('GALACT', models.CharField(blank=True, max_length=50, null=True)),
                ('FRUCT', models.CharField(blank=True, max_length=50, null=True)),
                ('SUCR', models.CharField(blank=True, max_length=50, null=True)),
                ('MALT', models.CharField(blank=True, max_length=50, null=True)),
                ('LACT', models.CharField(blank=True, max_length=50, null=True)),
                ('ALCO', models.CharField(blank=True, max_length=50, null=True)),
                ('ENGFIB', models.CharField(blank=True, max_length=50, null=True)),
                ('AOACFIB', models.CharField(blank=True, max_length=50, null=True)),
                ('SATFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTn6PFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTn3PFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('MONOFODc', models.CharField(blank=True, max_length=50, null=True)),
                ('MONOFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('POLYFODc', models.CharField(blank=True, max_length=50, null=True)),
                ('POLYFOD', models.CharField(blank=True, max_length=50, null=True)),
                ('SATFODx6', models.CharField(blank=True, max_length=50, null=True)),
                ('TOTBRFOD_g', models.CharField(blank=True, max_length=50, null=True)),
                ('FODTRANS_g', models.CharField(blank=True, max_length=50, null=True)),
                ('CHOL_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('K_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('CA_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('MG_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('P_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('FE_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('CU_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('ZN_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('CL_mg', models.CharField(blank=True, max_length=50, null=True)),
                ('MN', models.CharField(blank=True, max_length=50, null=True)),
                ('SE', models.CharField(blank=True, max_length=50, null=True)),
                ('I_mug', models.CharField(blank=True, max_length=50, null=True)),
                ('RET', models.CharField(blank=True, max_length=50, null=True)),
                ('CAREQU', models.CharField(blank=True, max_length=50, null=True)),
                ('RETEQU', models.CharField(blank=True, max_length=50, null=True)),
                ('VITD', models.CharField(blank=True, max_length=50, null=True)),
                ('VITE', models.CharField(blank=True, max_length=50, null=True)),
                ('VITK1', models.CharField(blank=True, max_length=50, null=True)),
                ('THIA', models.CharField(blank=True, max_length=50, null=True)),
                ('RIBO', models.CharField(blank=True, max_length=50, null=True)),
                ('NIAC', models.CharField(blank=True, max_length=50, null=True)),
                ('TRYP60', models.CharField(blank=True, max_length=50, null=True)),
                ('NIACEQU', models.CharField(blank=True, max_length=50, null=True)),
                ('VITB6', models.CharField(blank=True, max_length=50, null=True)),
                ('VITB12', models.CharField(blank=True, max_length=50, null=True)),
                ('FOLT', models.CharField(blank=True, max_length=50, null=True)),
                ('PANTO', models.CharField(blank=True, max_length=50, null=True)),
                ('BIOT', models.CharField(blank=True, max_length=50, null=True)),
                ('VITC', models.CharField(blank=True, max_length=50, null=True)),
                ('ALTRET', models.CharField(blank=True, max_length=50, null=True)),
                ('CISRET_13', models.CharField(blank=True, max_length=50, null=True)),
                ('DEHYRET', models.CharField(blank=True, max_length=50, null=True)),
                ('RETALD', models.CharField(blank=True, max_length=50, null=True)),
                ('ACAR', models.CharField(blank=True, max_length=50, null=True)),
                ('BCAR', models.CharField(blank=True, max_length=50, null=True)),
                ('CRYPT', models.CharField(blank=True, max_length=50, null=True)),
                ('LUT', models.CharField(blank=True, max_length=50, null=True)),
                ('LYCO', models.CharField(blank=True, max_length=50, null=True)),
                ('OHD3_25', models.CharField(blank=True, max_length=50, null=True)),
                ('VITD3', models.CharField(blank=True, max_length=50, null=True)),
                ('METHF_5', models.CharField(blank=True, max_length=50, null=True)),
                ('ATOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('BTOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('DTOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('GTOPH', models.CharField(blank=True, max_length=50, null=True)),
                ('ATOTR', models.CharField(blank=True, max_length=50, null=True)),
                ('GTOTR', models.CharField(blank=True, max_length=50, null=True)),
                ('Total_PHYTO', models.CharField(blank=True, max_length=50, null=True)),
                ('PHYTO', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Macro Nutrition',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('picture', models.ImageField(upload_to='media/recipe/')),
                ('picture_url', models.URLField(blank=True, null=True)),
                ('prep_time', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('prep_time_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('servings', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('steps1', models.TextField(blank=True, null=True)),
                ('steps2', models.TextField(blank=True, null=True)),
                ('steps3', models.TextField(blank=True, null=True)),
                ('steps4', models.TextField(blank=True, null=True)),
                ('steps5', models.TextField(blank=True, null=True)),
                ('steps6', models.TextField(blank=True, null=True)),
                ('steps7', models.TextField(blank=True, null=True)),
                ('steps8', models.TextField(blank=True, null=True)),
                ('steps9', models.TextField(blank=True, null=True)),
                ('steps10', models.TextField(blank=True, null=True)),
                ('steps11', models.TextField(blank=True, null=True)),
                ('steps12', models.TextField(blank=True, null=True)),
                ('steps13', models.TextField(blank=True, null=True)),
                ('steps14', models.TextField(blank=True, null=True)),
                ('steps15', models.TextField(blank=True, null=True)),
                ('steps_other', models.TextField(blank=True, null=True, verbose_name='Other Remaining steps')),
                ('recipe_by', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.ManyToManyField(blank=True, to='master.CategoryMaster')),
                ('nutrition', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='food.nutrition')),
                ('tag', models.ManyToManyField(blank=True, to='master.TagMaster')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.recipe')),
                ('tag', models.ManyToManyField(blank=True, to='master.TagMaster')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('prefer_time', models.CharField(choices=[('BF', 'Breakfast'), ('BR', 'Brunch'), ('LU', 'Lunch'), ('ES', 'Eve Snack'), ('DN', 'Dinner')], max_length=2)),
                ('intake_duration', models.PositiveSmallIntegerField(default=10, help_text='In Minutes')),
                ('food', models.ManyToManyField(blank=True, to='food.Food')),
                ('recipe', models.ManyToManyField(blank=True, to='food.Recipe')),
                ('tag', models.ManyToManyField(blank=True, to='master.TagMaster')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='alias_name',
            field=models.ManyToManyField(blank=True, to='food.IngredientAlias'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='food',
            name='ingredient',
            field=models.ManyToManyField(blank=True, to='food.Ingredient'),
        ),
        migrations.AddField(
            model_name='food',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
    ]