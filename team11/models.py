import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


class AnalysisStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    IN_PROGRESS = 'in_progress', 'In Progress'
    COMPLETED = 'completed', 'Completed'
    FAILED = 'failed', 'Failed'


class SubmissionType(models.TextChoices):
    WRITING = 'writing', 'Writing'
    LISTENING = 'listening', 'Listening'


class Submission(models.Model):
    """Abstract base model for all submissions"""
    submission_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(db_index=True)
    submission_type = models.CharField(max_length=20, choices=SubmissionType.choices)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    overall_score = models.FloatField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=AnalysisStatus.choices,
        default=AnalysisStatus.PENDING
    )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at', 'user_id']),
        ]

    def __str__(self):
        return f"{self.submission_type} - {self.submission_id}"


class WritingSubmission(models.Model):
    """Model for writing task submissions"""
    submission = models.OneToOneField(
        Submission,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='writing_details'
    )
    topic = models.CharField(max_length=500)
    text_body = models.TextField()
    word_count = models.PositiveIntegerField()

    def __str__(self):
        return f"Writing: {self.topic[:50]}"


class ListeningSubmission(models.Model):
    """Model for listening (speaking) task submissions"""
    submission = models.OneToOneField(
        Submission,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='listening_details'
    )
    topic = models.CharField(max_length=500)
    audio_file_url = models.CharField(max_length=500)
    duration_seconds = models.PositiveIntegerField()
    transcription = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Listening: {self.topic[:50]}"


class AssessmentResult(models.Model):
    """Model for assessment results with detailed scoring and feedback"""
    result_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    submission = models.OneToOneField(
        Submission,
        on_delete=models.CASCADE,
        related_name='assessment_result'
    )
    
    # Sub-scores stored as JSON
    grammar_score = models.FloatField(null=True, blank=True)
    vocabulary_score = models.FloatField(null=True, blank=True)
    coherence_score = models.FloatField(null=True, blank=True)
    fluency_score = models.FloatField(null=True, blank=True)
    pronunciation_score = models.FloatField(null=True, blank=True)
    
    # Feedback
    feedback_summary = models.TextField(blank=True)
    suggestions = models.JSONField(default=list, blank=True)
    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Assessment for {self.submission.submission_id}"
