# Create your models here.

import uuid

from django.db import models


class AppPurpose(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=uuid.uuid4,
        editable=False,
        name='id'
    )
    name = models.CharField(
        max_length=255,
        name='name'
    )
    description = models.TextField(
        blank=True,
        null=True,
        name='description'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        name='updated_at'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_purpose'


class LearningCategory(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=uuid.uuid4,
        editable=False,
        name='id'
    )
    category_purpose = models.ForeignKey(
        AppPurpose,
        on_delete=models.CASCADE,
        related_name='learning_categories',
        name='category_purpose'
    )
    category_name = models.CharField(
        max_length=255,
        name='category_name'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        name='updated_at'
    )
    created_by = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='created_by'
    )
    updated_by = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='updated_by'
    )

    def __str__(self):
        return f"{self.category_purpose} - {self.category_name}"

    class Meta:
        db_table = 'learning_category'


class ContentLearningModels(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=uuid.uuid4,
        editable=False,
        name='id'
    )
    model_provider = models.CharField(
        max_length=255,
        name='model_provider'
    )
    model_category = models.CharField(
        max_length=255,
        name='model_category'
    )
    model_sub_category = models.CharField(
        max_length=255,
        name='model_sub_category'
    )
    model_purpose = models.ForeignKey(
        AppPurpose,
        on_delete=models.CASCADE,
        related_name='content_learning_models',
        name='model_purpose'
    )
    model_name = models.CharField(
        max_length=255,
        name='model_name'
    )
    model_description = models.TextField(
        blank=True,
        null=True,
        name='model_description'
    )
    model_link = models.URLField(
        max_length=2000,
        blank=True,
        null=True,
        name='model_link'
    )
    model_keywords = models.JSONField(
        name='model_keywords'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        name='updated_at'
    )
    created_by = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='created_by'
    )
    updated_by = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='updated_by'
    )

    def __str__(self):
        return f"{self.model_provider} - {self.model_name}"

    class Meta:
        db_table = 'content_learning_models'


class Content(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=uuid.uuid4,
        editable=False,
        name='id'
    )
    content_type = models.CharField(
        max_length=100,
        name='content_type'
    )
    content_author = models.CharField(
        max_length=100,
        name='content_author'
    )
    content_author_sub_type = models.CharField(
        max_length=255,
        name='content_author_sub_type'
    )
    content_feature = models.CharField(
        max_length=255,
        name='content_feature'
    )
    content_sub_feature = models.CharField(
        max_length=255,
        name='content_sub_feature'
    )
    content_sub_feature_level_1 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='content_sub_feature_level_1'
    )
    content_sub_feature_level_2 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='content_sub_feature_level_2'
    )
    content_sub_feature_level_3 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='content_sub_feature_level_3'
    )
    content_sub_feature_level_4 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='content_sub_feature_level_4'
    )
    content_sub_feature_level_5 = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='content_sub_feature_level_5'
    )
    content_keywords = models.JSONField(
        name='content_keywords'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        name='updated_at'
    )
    created_by = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='created_by'
    )
    updated_by = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        name='updated_by'
    )

    def __str__(self):
        return f"{self.content_author} - {self.content_feature} - {self.content_sub_feature}"

    class Meta:
        db_table = 'content'
