# In Homepage or Mediaplayer/management/commands/run_speech.py
from django.core.management.base import BaseCommand
from scripts.speech import main as speech_main

class Command(BaseCommand):
    help = 'Runs the speech script'

    def handle(self, *args, **options):
        speech_main()
