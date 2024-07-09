# Register your models here.

from django.contrib import admin

from .models import AppPurpose, LearningCategory, ContentLearningModels, Content


@admin.register(AppPurpose)
class AppPurposeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')


@admin.register(LearningCategory)
class LearningCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_purpose', 'category_name', 'created_at', 'updated_at')
    search_fields = ('category_purpose__name', 'category_name')
    list_filter = ('category_purpose', 'created_at', 'updated_at')


@admin.register(ContentLearningModels)
class ContentLearningModelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_provider', 'model_name', 'model_purpose', 'created_at', 'updated_at')
    search_fields = ('model_provider', 'model_name', 'model_purpose__name')
    list_filter = ('model_provider', 'model_purpose', 'created_at', 'updated_at')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'content_author', 'content_feature', 'created_at', 'updated_at')
    search_fields = ('content_type', 'content_author', 'content_feature')
    list_filter = ('content_author', 'created_at', 'updated_at')
