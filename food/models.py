from django.db import models

from master.models import TagMaster, CategoryMaster


class Nutrition(models.Model):
    protein_g = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=False, null=False)
    carbohydrate_g = models.FloatField(blank=True, null=True)
    calcium_g = models.FloatField(blank=True, null=True)
    # is_active = models.BooleanField(default=True)
    calories_from_fat = models.FloatField(blank=True, null=True)
    total_fat_g = models.FloatField(blank=True, null=True)
    total_fat_dv = models.FloatField(blank=True, null=True)
    sodium_g = models.FloatField(blank=True, null=True)
    sodium_dv = models.FloatField(blank=True, null=True)
    potassium_g = models.FloatField(blank=True, null=True)
    potassium_dv = models.FloatField(blank=True, null=True)
    carbohydrate_dv = models.FloatField(blank=True, null=True)
    dietary_fiber_g = models.FloatField(blank=True, null=True)
    dietary_fiber_dv = models.FloatField(blank=True, null=True)
    sugar_g = models.FloatField(blank=True, null=True)
    Vitamin_A_dv = models.FloatField(blank=True, null=True)
    Vitamin_C_dv = models.FloatField(blank=True, null=True)
    calcium_dv = models.FloatField(blank=True, null=True)
    iron_dv = models.FloatField(blank=True, null=True)
    saturated_fat_dv = models.FloatField(blank=True, null=True)
    saturated_fat_mg = models.FloatField(blank=True, null=True)
    cholesterol_dv = models.FloatField(blank=True, null=True)
    cholesterol_mg = models.FloatField(blank=True, null=True)
    Food_Code = models.CharField(max_length=200, blank=True, null=True)
    Total_solids = models.CharField(max_length=20, blank=True, null=True)
    Nitrogen_conversion_factor = models.CharField(max_length=50, blank=True, null=True)
    Glycerol_conversion_factor = models.CharField(max_length=50, blank=True, null=True)
    WATER = models.CharField(max_length=50, blank=True, null=True)
    FAT_g = models.CharField(max_length=50, blank=True, null=True)
    Energy_kj = models.CharField(max_length=50, blank=True, null=True)
    Starch_g = models.CharField(max_length=50, blank=True, null=True)
    OLIGO_g = models.CharField(max_length=50, blank=True, null=True)
    TOTSUG = models.CharField(max_length=50, blank=True, null=True)
    GLUC = models.CharField(max_length=50, blank=True, null=True)
    GALACT = models.CharField(max_length=50, blank=True, null=True)
    FRUCT = models.CharField(max_length=50, blank=True, null=True)
    SUCR = models.CharField(max_length=50, blank=True, null=True)
    MALT = models.CharField(max_length=50, blank=True, null=True)
    LACT = models.CharField(max_length=50, blank=True, null=True)
    ALCO = models.CharField(max_length=50, blank=True, null=True)
    ENGFIB = models.CharField(max_length=50, blank=True, null=True)
    AOACFIB = models.CharField(max_length=50, blank=True, null=True)
    SATFOD = models.CharField(max_length=50, blank=True, null=True)
    TOTn6PFOD = models.CharField(max_length=50, blank=True, null=True)
    TOTn3PFOD = models.CharField(max_length=50, blank=True, null=True)
    MONOFODc = models.CharField(max_length=50, blank=True, null=True)
    MONOFOD = models.CharField(max_length=50, blank=True, null=True)
    POLYFODc = models.CharField(max_length=50, blank=True, null=True)
    POLYFOD = models.CharField(max_length=50, blank=True, null=True)
    SATFODx6 = models.CharField(max_length=50, blank=True, null=True)
    TOTBRFOD_g = models.CharField(max_length=50, blank=True, null=True)
    FODTRANS_g = models.CharField(max_length=50, blank=True, null=True)
    CHOL_mg = models.CharField(max_length=50, blank=True, null=True)
    K_mg = models.CharField(max_length=50, blank=True, null=True)
    CA_mg = models.CharField(max_length=50, blank=True, null=True)
    MG_mg = models.CharField(max_length=50, blank=True, null=True)
    P_mg = models.CharField(max_length=50, blank=True, null=True)
    FE_mg = models.CharField(max_length=50, blank=True, null=True)
    CU_mg = models.CharField(max_length=50, blank=True, null=True)
    ZN_mg = models.CharField(max_length=50, blank=True, null=True)
    CL_mg = models.CharField(max_length=50, blank=True, null=True)
    MN = models.CharField(max_length=50, blank=True, null=True)
    SE = models.CharField(max_length=50, blank=True, null=True)
    I_mug = models.CharField(max_length=50, blank=True, null=True)
    RET = models.CharField(max_length=50, blank=True, null=True)
    CAREQU = models.CharField(max_length=50, blank=True, null=True)
    RETEQU = models.CharField(max_length=50, blank=True, null=True)
    VITD = models.CharField(max_length=50, blank=True, null=True)
    VITE = models.CharField(max_length=50, blank=True, null=True)
    VITK1 = models.CharField(max_length=50, blank=True, null=True)
    THIA = models.CharField(max_length=50, blank=True, null=True)
    RIBO = models.CharField(max_length=50, blank=True, null=True)
    NIAC = models.CharField(max_length=50, blank=True, null=True)
    TRYP60 = models.CharField(max_length=50, blank=True, null=True)
    NIACEQU = models.CharField(max_length=50, blank=True, null=True)
    VITB6 = models.CharField(max_length=50, blank=True, null=True)
    VITB12 = models.CharField(max_length=50, blank=True, null=True)
    FOLT = models.CharField(max_length=50, blank=True, null=True)
    PANTO = models.CharField(max_length=50, blank=True, null=True)
    BIOT = models.CharField(max_length=50, blank=True, null=True)
    VITC = models.CharField(max_length=50, blank=True, null=True)
    ALTRET = models.CharField(max_length=50, blank=True, null=True)
    CISRET_13 = models.CharField(max_length=50, blank=True, null=True)
    DEHYRET = models.CharField(max_length=50, blank=True, null=True)
    RETALD = models.CharField(max_length=50, blank=True, null=True)
    ACAR = models.CharField(max_length=50, blank=True, null=True)
    BCAR = models.CharField(max_length=50, blank=True, null=True)
    CRYPT = models.CharField(max_length=50, blank=True, null=True)
    LUT = models.CharField(max_length=50, blank=True, null=True)
    LYCO = models.CharField(max_length=50, blank=True, null=True)
    OHD3_25 = models.CharField(max_length=50, blank=True, null=True)
    VITD3 = models.CharField(max_length=50, blank=True, null=True)
    METHF_5 = models.CharField(max_length=50, blank=True, null=True)
    ATOPH = models.CharField(max_length=50, blank=True, null=True)
    BTOPH = models.CharField(max_length=50, blank=True, null=True)
    DTOPH = models.CharField(max_length=50, blank=True, null=True)
    GTOPH = models.CharField(max_length=50, blank=True, null=True)
    ATOTR = models.CharField(max_length=50, blank=True, null=True)
    GTOTR = models.CharField(max_length=50, blank=True, null=True)
    Total_PHYTO = models.CharField(max_length=50, blank=True, null=True)
    PHYTO = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Macro Nutrition'


class IngredientAlias(models.Model):
    name = models.CharField(verbose_name="Ingredient Alias name", max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(verbose_name="Ingredient for the Recipe", max_length=100, unique=True)
    alias_name = models.ManyToManyField(IngredientAlias, blank=True)
    unit = models.CharField(blank=True, null=True, max_length=50)
    quantity = models.FloatField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)
    protein_g = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=False, null=False)
    carbohydrate_g = models.FloatField(blank=True, null=True)
    calcium_g = models.FloatField(blank=True, null=True)
    # is_active = models.BooleanField(default=True)
    calories_from_fat = models.FloatField(blank=True, null=True)
    total_fat_g = models.FloatField(blank=True, null=True)
    total_fat_dv = models.FloatField(blank=True, null=True)
    sodium_g = models.FloatField(blank=True, null=True)
    sodium_dv = models.FloatField(blank=True, null=True)
    potassium_g = models.FloatField(blank=True, null=True)
    potassium_dv = models.FloatField(blank=True, null=True)
    carbohydrate_dv = models.FloatField(blank=True, null=True)
    dietary_fiber_g = models.FloatField(blank=True, null=True)
    dietary_fiber_dv = models.FloatField(blank=True, null=True)
    sugar_g = models.FloatField(blank=True, null=True)
    Vitamin_A_dv = models.FloatField(blank=True, null=True)
    Vitamin_C_dv = models.FloatField(blank=True, null=True)
    calcium_dv = models.FloatField(blank=True, null=True)
    iron_dv = models.FloatField(blank=True, null=True)
    saturated_fat_dv = models.FloatField(blank=True, null=True)
    saturated_fat_mg = models.FloatField(blank=True, null=True)
    cholesterol_dv = models.FloatField(blank=True, null=True)
    cholesterol_mg = models.FloatField(blank=True, null=True)
    Food_Code = models.CharField(max_length=200, blank=True, null=True)
    Total_solids = models.CharField(max_length=20, blank=True, null=True)
    Nitrogen_conversion_factor = models.CharField(max_length=50, blank=True, null=True)
    Glycerol_conversion_factor = models.CharField(max_length=50, blank=True, null=True)
    WATER = models.CharField(max_length=50, blank=True, null=True)
    FAT_g = models.CharField(max_length=50, blank=True, null=True)
    Energy_kj = models.CharField(max_length=50, blank=True, null=True)
    Starch_g = models.CharField(max_length=50, blank=True, null=True)
    OLIGO_g = models.CharField(max_length=50, blank=True, null=True)
    TOTSUG = models.CharField(max_length=50, blank=True, null=True)
    GLUC = models.CharField(max_length=50, blank=True, null=True)
    GALACT = models.CharField(max_length=50, blank=True, null=True)
    FRUCT = models.CharField(max_length=50, blank=True, null=True)
    SUCR = models.CharField(max_length=50, blank=True, null=True)
    MALT = models.CharField(max_length=50, blank=True, null=True)
    LACT = models.CharField(max_length=50, blank=True, null=True)
    ALCO = models.CharField(max_length=50, blank=True, null=True)
    ENGFIB = models.CharField(max_length=50, blank=True, null=True)
    AOACFIB = models.CharField(max_length=50, blank=True, null=True)
    SATFOD = models.CharField(max_length=50, blank=True, null=True)
    TOTn6PFOD = models.CharField(max_length=50, blank=True, null=True)
    TOTn3PFOD = models.CharField(max_length=50, blank=True, null=True)
    MONOFODc = models.CharField(max_length=50, blank=True, null=True)
    MONOFOD = models.CharField(max_length=50, blank=True, null=True)
    POLYFODc = models.CharField(max_length=50, blank=True, null=True)
    POLYFOD = models.CharField(max_length=50, blank=True, null=True)
    SATFODx6 = models.CharField(max_length=50, blank=True, null=True)
    TOTBRFOD_g = models.CharField(max_length=50, blank=True, null=True)
    FODTRANS_g = models.CharField(max_length=50, blank=True, null=True)
    CHOL_mg = models.CharField(max_length=50, blank=True, null=True)
    K_mg = models.CharField(max_length=50, blank=True, null=True)
    CA_mg = models.CharField(max_length=50, blank=True, null=True)
    MG_mg = models.CharField(max_length=50, blank=True, null=True)
    P_mg = models.CharField(max_length=50, blank=True, null=True)
    FE_mg = models.CharField(max_length=50, blank=True, null=True)
    CU_mg = models.CharField(max_length=50, blank=True, null=True)
    ZN_mg = models.CharField(max_length=50, blank=True, null=True)
    CL_mg = models.CharField(max_length=50, blank=True, null=True)
    MN = models.CharField(max_length=50, blank=True, null=True)
    SE = models.CharField(max_length=50, blank=True, null=True)
    I_mug = models.CharField(max_length=50, blank=True, null=True)
    RET = models.CharField(max_length=50, blank=True, null=True)
    CAREQU = models.CharField(max_length=50, blank=True, null=True)
    RETEQU = models.CharField(max_length=50, blank=True, null=True)
    VITD = models.CharField(max_length=50, blank=True, null=True)
    VITE = models.CharField(max_length=50, blank=True, null=True)
    VITK1 = models.CharField(max_length=50, blank=True, null=True)
    THIA = models.CharField(max_length=50, blank=True, null=True)
    RIBO = models.CharField(max_length=50, blank=True, null=True)
    NIAC = models.CharField(max_length=50, blank=True, null=True)
    TRYP60 = models.CharField(max_length=50, blank=True, null=True)
    NIACEQU = models.CharField(max_length=50, blank=True, null=True)
    VITB6 = models.CharField(max_length=50, blank=True, null=True)
    VITB12 = models.CharField(max_length=50, blank=True, null=True)
    FOLT = models.CharField(max_length=50, blank=True, null=True)
    PANTO = models.CharField(max_length=50, blank=True, null=True)
    BIOT = models.CharField(max_length=50, blank=True, null=True)
    VITC = models.CharField(max_length=50, blank=True, null=True)
    ALTRET = models.CharField(max_length=50, blank=True, null=True)
    CISRET_13 = models.CharField(max_length=50, blank=True, null=True)
    DEHYRET = models.CharField(max_length=50, blank=True, null=True)
    RETALD = models.CharField(max_length=50, blank=True, null=True)
    ACAR = models.CharField(max_length=50, blank=True, null=True)
    BCAR = models.CharField(max_length=50, blank=True, null=True)
    CRYPT = models.CharField(max_length=50, blank=True, null=True)
    LUT = models.CharField(max_length=50, blank=True, null=True)
    LYCO = models.CharField(max_length=50, blank=True, null=True)
    OHD3_25 = models.CharField(max_length=50, blank=True, null=True)
    VITD3 = models.CharField(max_length=50, blank=True, null=True)
    METHF_5 = models.CharField(max_length=50, blank=True, null=True)
    ATOPH = models.CharField(max_length=50, blank=True, null=True)
    BTOPH = models.CharField(max_length=50, blank=True, null=True)
    DTOPH = models.CharField(max_length=50, blank=True, null=True)
    GTOPH = models.CharField(max_length=50, blank=True, null=True)
    ATOTR = models.CharField(max_length=50, blank=True, null=True)
    GTOTR = models.CharField(max_length=50, blank=True, null=True)
    Total_PHYTO = models.CharField(max_length=50, blank=True, null=True)
    PHYTO = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(verbose_name="title", max_length=100)
    category = models.ManyToManyField(CategoryMaster, blank=True)
    picture = models.ImageField(upload_to='media/recipe/', blank=False, null=False)
    picture_url = models.URLField(blank=True, null=True)
    prep_time = models.PositiveSmallIntegerField(blank=True, null=True)
    prep_time_unit = models.CharField(max_length=50, blank=True, null=True)
    servings = models.CharField(max_length=50, blank=True, null=True)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.DO_NOTHING)
    details = models.TextField(blank=True, null=True)
    steps1 = models.TextField(blank=True, null=True)
    steps2 = models.TextField(blank=True, null=True)
    steps3 = models.TextField(blank=True, null=True)
    steps4 = models.TextField(blank=True, null=True)
    steps5 = models.TextField(blank=True, null=True)
    steps6 = models.TextField(blank=True, null=True)
    steps7 = models.TextField(blank=True, null=True)
    steps8 = models.TextField(blank=True, null=True)
    steps9 = models.TextField(blank=True, null=True)
    steps10 = models.TextField(blank=True, null=True)
    steps11 = models.TextField(blank=True, null=True)
    steps12 = models.TextField(blank=True, null=True)
    steps13 = models.TextField(blank=True, null=True)
    steps14 = models.TextField(blank=True, null=True)
    steps15 = models.TextField(blank=True, null=True)
    steps_other = models.TextField("Other Remaining steps", blank=True, null=True)
    recipe_by = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return '%s' % self.title


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    qty = models.PositiveSmallIntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return '%s for %s' % (self.ingredient.name, self.recipe.title)


class Food(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity_g = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    ingredient = models.ManyToManyField(Ingredient, blank=True)
    # recipe = models.ManyToManyField(Recipe, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return '%s' % self.name


class Meal_Type(models.TextChoices):
    BREAKFAST = 'BF'
    BRUNCH = 'BR'
    LUNCH = 'LU'
    EVE_SNACK = 'ES'
    DINNER = 'DN'


class Meal(models.Model):
    title = models.CharField(max_length=50)
    prefer_time = models.CharField(max_length=2, choices=Meal_Type.choices)
    food = models.ManyToManyField(Food, blank=True)
    recipe = models.ManyToManyField(Recipe, blank=True)
    intake_duration = models.PositiveSmallIntegerField(help_text="In Minutes", default=10)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return self.title


# class Cycle(models.Model):
#     actual_cycle_start = models.DateField()
#     actual_cycle_end = models.DateField(blank=True, null=True)
#     predicted_cycle_start = models.DateField(blank=True, null=True)
#     predicted_cycle_end = models.DateField(blank=True, null=True)
#
#
# class CycleUser(models.Model):
#     cycle_start_date = models.DateField()
#     cycle_end_date = models.DateField(blank=True, null=True)
#     dates = models.ForeignKey(Cycle, blank=True, null=True)



