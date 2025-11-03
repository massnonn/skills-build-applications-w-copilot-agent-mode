from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Cancella tutti i dati esistenti
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Crea Team
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Crea Utenti (supereroi)
        ironman = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Crea Workout
        pushups = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        situps = Workout.objects.create(name='Situps', description='Do situps', difficulty='Medium')
        running = Workout.objects.create(name='Running', description='Run 5km', difficulty='Hard')

        # Crea Activity
        Activity.objects.create(user=ironman, workout=pushups, date=timezone.now(), duration_minutes=30, calories_burned=200)
        Activity.objects.create(user=spiderman, workout=situps, date=timezone.now(), duration_minutes=20, calories_burned=150)
        Activity.objects.create(user=batman, workout=running, date=timezone.now(), duration_minutes=40, calories_burned=400)
        Activity.objects.create(user=superman, workout=pushups, date=timezone.now(), duration_minutes=25, calories_burned=180)

        # Crea Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=350, position=1)
        Leaderboard.objects.create(team=dc, total_points=580, position=2)

        self.stdout.write(self.style.SUCCESS('Database popolato con dati di test (supereroi, team marvel e dc).'))
