import os
from optparse import make_option

from django.utils.text import slugify
from django.db.models.loading import get_model
from django.core.management.base import BaseCommand, CommandError

from tqdm import tqdm


class Command(BaseCommand):
    help = "Command to import words into database."
    args = ('f',)
    option_list = BaseCommand.option_list + (
        make_option(
            "-f",
            "--file",
            dest="filename",
            help="specify import file",
            metavar="FILE"
        ),
    )

    def handle(self, *args, **options):
        if options['filename'] == None:
            raise CommandError("Option `--file=...` must be specified.")

        if not os.path.isfile(options['filename']):
            raise CommandError("File does not exist at the specified path.")

        UrlSlug = get_model(app_label='shorter', model_name='UrlSlug')

        with open(options['filename'], 'r') as input_file:
            for line in tqdm(input_file.readlines()):
                url_slug, created = UrlSlug.objects.get_or_create(**{
                    'slug': slugify(line),
                    'word': line
                })
