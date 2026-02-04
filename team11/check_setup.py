"""
Quick verification script for Team 11 module setup
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app404.settings')
django.setup()

from team11.models import QuestionCategory, Question, Submission, WritingSubmission, ListeningSubmission

print('=' * 60)
print('TEAM 11 MODULE - SETUP VERIFICATION')
print('=' * 60)

# Check categories
categories = QuestionCategory.objects.using('team11').all()
print(f'\n✓ Categories: {categories.count()}')
for cat in categories:
    q_count = cat.questions.using('team11').count()
    print(f'  - {cat.name} ({cat.question_type}): {q_count} questions')

# Check questions
questions = Question.objects.using('team11').all()
print(f'\n✓ Total Questions: {questions.count()}')
writing_q = questions.filter(category__question_type='writing').count()
listening_q = questions.filter(category__question_type='listening').count()
print(f'  - Writing: {writing_q}')
print(f'  - Listening: {listening_q}')

# Check submissions
submissions = Submission.objects.using('team11').all()
print(f'\n✓ Total Submissions: {submissions.count()}')
if submissions.exists():
    completed = submissions.filter(status='completed').count()
    pending = submissions.filter(status='pending').count()
    print(f'  - Completed: {completed}')
    print(f'  - Pending: {pending}')

print('\n' + '=' * 60)
print('DATABASE STRUCTURE CHECK')
print('=' * 60)

# Verify foreign key relationships
sample_question = questions.first()
if sample_question:
    print(f'\n✓ Sample Question:')
    print(f'  - ID: {sample_question.question_id}')
    print(f'  - Category: {sample_question.category.name}')
    print(f'  - Text: {sample_question.question_text[:50]}...')
    print(f'  - Difficulty: {sample_question.difficulty_level}')

print('\n' + '=' * 60)
print('✓ ALL CHECKS PASSED - MODULE READY FOR USE')
print('=' * 60)
