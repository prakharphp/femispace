from django.db import models


class TagMasterChoices(models.IntegerChoices):
    symptoms = 1
    Cycle = 2


class TagMaster(models.Model):
    tag_type = models.PositiveSmallIntegerField(choices=TagMasterChoices.choices, default=TagMasterChoices.symptoms)
    name = models.CharField(verbose_name="Tag name", max_length=100)

    def __str__(self):
        return self.name


class CategoryMaster(models.Model):
    title = models.CharField(verbose_name="Category Title", max_length=100)

    def __str__(self):
        return self.title


class TypeChoices(models.IntegerChoices):
    Dashboard = 1
    Pop_up = 2


class Banners(models.Model):
    type = models.PositiveSmallIntegerField(choices=TypeChoices.choices, default=TypeChoices.Dashboard)
    order = models.PositiveSmallIntegerField(blank=True, null=True)
    url_redirect_key = models.CharField(max_length=50)
    image = models.FileField()
    is_active = models.BooleanField(default=False)


class HealthCourses(models.Model):
    title = models.CharField(max_length=30)
    image = models.URLField()
    created_by = models.CharField(max_length=10)
    duration_min = models.PositiveSmallIntegerField(blank=True, null=True)


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    introduction = models.TextField()
    biology = models.TextField()
    how_to_measure = models.TextField()
    order = models.PositiveSmallIntegerField()
    courses = models.ForeignKey(HealthCourses, on_delete=models.CASCADE, blank=True, null=True)


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


class ActivityMaster(models.Model):
    title = models.CharField(verbose_name="Activity Title", max_length=100)
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return self.title


class ExerciseMaster(models.Model):
    title = models.CharField(verbose_name="Exercise Title", max_length=100)
    category = models.CharField(verbose_name="Exercise Category", max_length=100, blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    image_link = models.URLField(blank=True, null=True)
    duration_min = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    difficulty_level = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Please enter the difficulty level for the exercise")
    ordering = models.PositiveSmallIntegerField(blank=True, null=True)
    tag_master = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return '%s' % self.title


class ExerciseActivityMaster(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    exercise = models.ManyToManyField(ExerciseMaster, blank=True)
    duration_min = models.PositiveSmallIntegerField(blank=True, null=True)
    calories_burn = models.PositiveIntegerField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)
    # day_order

    def __str__(self):
        return '%s' % self.name


class EatRainbowMaster(models.Model):
    title = models.CharField(max_length=50)
    red_serving = models.PositiveSmallIntegerField(default=0)
    cream_serving = models.PositiveSmallIntegerField(default=0)
    yellow_serving = models.PositiveSmallIntegerField(default=0)
    kiwi_serving = models.PositiveSmallIntegerField(default=0)
    blue_serving = models.PositiveSmallIntegerField(default=0)
    green_serving = models.PositiveSmallIntegerField(default=0)
    enjoy_regular = models.ManyToManyField(Food, blank=True, related_name="enjoy_regular_master")
    eat_more = models.ManyToManyField(Food, blank=True, related_name="eat_more_master")
    eat_less = models.ManyToManyField(Food, blank=True, related_name="eat_less_master")
    eat_avoid = models.ManyToManyField(Food, verbose_name="Avoid eat", blank=True, related_name="eat_avoid_master")
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return '%s' % self.title


class DrinkingActivityMaster(models.Model):
    water = models.PositiveSmallIntegerField(default=5)
    soft_drink = models.PositiveSmallIntegerField(default=0)
    smoothie = models.PositiveSmallIntegerField(default=0)
    ice_tea = models.PositiveSmallIntegerField(default=0)
    fruit_juice = models.PositiveSmallIntegerField(default=0)
    coffee = models.PositiveSmallIntegerField(default=0)
    bear = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(TagMaster, blank=True)


class SugarIntakeActivityMaster(models.Model):
    fruits = models.ManyToManyField(Food, blank=True, related_name="fruits")
    dried_fruits = models.ManyToManyField(Food, blank=True, related_name="Dry_Fruits")
    sweet_veggie = models.ManyToManyField(Food, blank=True, related_name="sweet_vaggies")
    drink_juices = models.ManyToManyField(Food, blank=True, related_name="drink_juice")
    dessert_snack = models.ManyToManyField(Food, blank=True, related_name="dessert_snacks")
    sugar_intake = models.PositiveSmallIntegerField(default=0)
    calories_gained = models.PositiveSmallIntegerField(default=0)
    comments = models.TextField(blank=True, null=True)


class MeditationMaster(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    url = models.URLField()
    Description = models.TextField()


class Day(models.Model):
    title = models.CharField(max_length=50)
    activity = models.ManyToManyField(ActivityMaster, blank=True)
    breakfast_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="breakfast")
    brunch_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="brunch")
    lunch_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="lunch")
    eve_snacks_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="eve_snack")
    dinner_meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True, related_name="dinner")
    morning_exercise = models.ManyToManyField(ExerciseMaster, blank=True, related_name="morning_exercise_list")
    evening_exercise = models.ManyToManyField(ExerciseMaster, blank=True, related_name="evening_exercise_list")
    tag = models.ManyToManyField(TagMaster, blank=True)

    def __str__(self):
        return self.title


class Program(models.Model):
    title = models.CharField(max_length=50)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    days = models.ManyToManyField(Day)
    preferred_for = models.ManyToManyField('health.WellnessArea', blank=True)
    tag = models.ManyToManyField(TagMaster, blank=True)
    duration_in_days = models.CharField(max_length=50, default=7)
    # start_date = models.DateField()
    eat_rainbow = models.ForeignKey(EatRainbowMaster, on_delete=models.CASCADE, blank=True, null=True)
    exercise = models.ForeignKey(ExerciseActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    drinking_exercise = models.ForeignKey(DrinkingActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    sugar_intake = models.ForeignKey(SugarIntakeActivityMaster, on_delete=models.CASCADE, blank=True, null=True)
    meditation = models.ForeignKey(MeditationMaster, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def day_count(self):
        return len(self.days.all()) if self.days else 0

    def __str__(self):
        return self.title
