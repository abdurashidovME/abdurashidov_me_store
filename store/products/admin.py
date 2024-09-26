from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'queue', 'category')
    fields = ('image', 'name', 'description', ('price', 'queue'), 'stripe_product_price_id', 'category')
    # readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    filter = ('product', 'queue', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
