from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        self.assertEqual(str(team), 'Marvel')
    def test_user_create(self):
        team = Team.objects.create(name='DC', universe='DC')
        user = User.objects.create(email='batman@dc.com', username='Batman', team=team)
        self.assertEqual(str(user), 'Batman')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')
    def test_activity_create(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        user = User.objects.create(email='spiderman@marvel.com', username='Spiderman', team=team)
        workout = Workout.objects.create(name='Situps', description='Do situps', difficulty='Medium')
        activity = Activity.objects.create(user=user, workout=workout, date='2025-10-31T10:00:00Z', duration_minutes=30, calories_burned=200)
        self.assertEqual(str(activity), 'Spiderman - Situps')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, position=1)
        self.assertEqual(str(leaderboard), 'Marvel - 1')
