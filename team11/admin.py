from django.contrib import admin
from .models import Submission, WritingSubmission, ListeningSubmission, AssessmentResult


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['submission_id', 'user_id', 'submission_type', 'overall_score', 'status', 'created_at']
    list_filter = ['submission_type', 'status', 'created_at']
    search_fields = ['submission_id', 'user_id']
    readonly_fields = ['submission_id', 'created_at']
    ordering = ['-created_at']


@admin.register(WritingSubmission)
class WritingSubmissionAdmin(admin.ModelAdmin):
    list_display = ['submission', 'topic', 'word_count']
    search_fields = ['topic', 'text_body']
    readonly_fields = ['submission']


@admin.register(ListeningSubmission)
class ListeningSubmissionAdmin(admin.ModelAdmin):
    list_display = ['submission', 'topic', 'duration_seconds']
    search_fields = ['topic']
    readonly_fields = ['submission']


@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ['result_id', 'submission', 'created_at']
    readonly_fields = ['result_id', 'created_at']
    search_fields = ['submission__submission_id']
