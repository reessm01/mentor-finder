from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from mentor_finder.industry.models import Industry

class Command(BaseCommand):
    help = 'Intializes or adds personality types.'

    def handle(self, *args, **options):
        industries = [
            'Technology',
            'Personal'
        ]

        added = []

        try:
            for industry in industries:
                Industry.objects.create(
                    title=industry
                )
                added.append(industry)
        except IntegrityError:
            pass

        self.stdout.write(self.style.SUCCESS(f'Industry table rows added: {added}'))