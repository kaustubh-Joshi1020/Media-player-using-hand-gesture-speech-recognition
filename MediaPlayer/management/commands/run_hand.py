# In Homepage or Mediaplayer/management/commands/run_hand.py
from django.core.management.base import BaseCommand
from scripts.hand import main as hand_main

class Command(BaseCommand):
    help = 'Runs the hand script'

    def handle(self, *args, **options):
        hand_main()
