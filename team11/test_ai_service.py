"""
Test script for AI assessment services
Run this to verify the AI integration is working correctly
"""

import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Test without Django (standalone test)
from team11.services.ai_service import assess_writing

def test_writing_assessment():
    """Test writing assessment with a sample text"""
    print("=" * 60)
    print("Testing Writing Assessment")
    print("=" * 60)
    
    topic = "Describe your favorite holiday destination and explain why you enjoy it."
    text_body = """
    Paris is my favorite holiday destination because it combines history, culture, 
    and exceptional cuisine. The city offers countless museums like the Louvre and 
    Musée d'Orsay, where you can explore centuries of artistic achievement. Walking 
    along the Seine River at sunset provides a romantic atmosphere that is hard to 
    find elsewhere. The local cafés serve delicious pastries and coffee, making 
    every morning a delightful experience. Additionally, the architecture throughout 
    the city, from Gothic cathedrals to modern buildings, creates a unique visual 
    landscape. The public transportation system makes it easy to navigate, allowing 
    visitors to explore different neighborhoods efficiently. Overall, Paris offers 
    an unforgettable experience that appeals to travelers of all interests.
    """
    
    word_count = len(text_body.split())
    
    print(f"\nTopic: {topic}")
    print(f"Word Count: {word_count}")
    print("\nCalling AI assessment service...")
    
    result = assess_writing(topic, text_body, word_count)
    
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    if result['success']:
        print(f"✅ Assessment Successful!")
        print(f"\nOverall Score: {result['overall_score']}/100")
        print(f"\nSub-scores:")
        print(f"  - Grammar: {result['grammar_score']}/100")
        print(f"  - Vocabulary: {result['vocabulary_score']}/100")
        print(f"  - Coherence: {result['coherence_score']}/100")
        print(f"  - Fluency: {result['fluency_score']}/100")
        print(f"\nFeedback: {result['feedback_summary']}")
        print(f"\nSuggestions:")
        for i, suggestion in enumerate(result['suggestions'], 1):
            print(f"  {i}. {suggestion}")
    else:
        print(f"❌ Assessment Failed!")
        print(f"Error: {result.get('error', 'Unknown error')}")
    
    print("\n" + "=" * 60)


def test_speaking_assessment():
    """Test speaking assessment (requires an audio file)"""
    print("\n" + "=" * 60)
    print("Testing Speaking Assessment")
    print("=" * 60)
    
    print("\n⚠️  Speaking assessment requires an actual audio file.")
    print("To test speaking assessment:")
    print("1. Record a short audio file (mp3, wav, etc.)")
    print("2. Save it to a known location")
    print("3. Update the audio_file_path below")
    print("4. Uncomment and run the code")
    
    # Uncomment and modify this section when you have an audio file:
    """
    from team11.services.ai_service import assess_speaking
    
    topic = "Talk about your career goals and how you plan to achieve them."
    audio_file_path = "path/to/your/audio.mp3"  # Update this path
    duration_seconds = 45
    
    print(f"\nTopic: {topic}")
    print(f"Audio File: {audio_file_path}")
    print(f"Duration: {duration_seconds} seconds")
    print("\nCalling AI assessment service...")
    
    result = assess_speaking(topic, audio_file_path, duration_seconds)
    
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    if result['success']:
        print(f"✅ Assessment Successful!")
        print(f"\nTranscription: {result['transcription']}")
        print(f"\nOverall Score: {result['overall_score']}/100")
        print(f"\nSub-scores:")
        print(f"  - Pronunciation: {result['pronunciation_score']}/100")
        print(f"  - Fluency: {result['fluency_score']}/100")
        print(f"  - Vocabulary: {result['vocabulary_score']}/100")
        print(f"  - Grammar: {result['grammar_score']}/100")
        print(f"  - Coherence: {result['coherence_score']}/100")
        print(f"\nFeedback: {result['feedback_summary']}")
        print(f"\nSuggestions:")
        for i, suggestion in enumerate(result['suggestions'], 1):
            print(f"  {i}. {suggestion}")
    else:
        print(f"❌ Assessment Failed!")
        print(f"Error: {result.get('error', 'Unknown error')}")
    
    print("\n" + "=" * 60)
    """


if __name__ == "__main__":
    print("\n🚀 Starting AI Service Tests\n")
    
    # Test 1: Writing Assessment
    test_writing_assessment()
    
    # Test 2: Speaking Assessment (commented out - requires audio file)
    test_speaking_assessment()
    
    print("\n✅ All tests completed!\n")
