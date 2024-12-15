from django.db import models


class RestaurantModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
        db_table = 'restaurant'


class CategoryMenuModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category Menu'
        verbose_name_plural = 'Category Menus'
        db_table = 'category_menu'

class MenuModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    massa = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    category = models.ForeignKey(CategoryMenuModel, on_delete=models.CASCADE, related_name='category_menus')
    restaurants = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE, related_name='restaurant_menu')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        db_table = 'menu'

