from django.core.management.base import BaseCommand, CommandError
from aggregator.models import Feed, FeedItem

class Command(BaseCommand):
    args = '[feed_id feed_id ...]'
    help = 'Syncs either all or given feeds'

    def handle(self, *args, **options):
        if len(args):
            feeds = Feed.objects.filter(id__in=args)
        else:
            feeds = Feed.objects.all()
        for feed in feeds:
            # bump timestamp
            feed.status = 0
            feed.failures = 0
            feed.save()

            self.stdout.write('Successfully synced feed "%s"' % feed.id)