import csv
from django.core.management import BaseCommand, CommandError
from os.path import abspath
from sightings.models import Sighting


def _format_unique_squirrel_id(value):
    if value is None:
        return ''

    return str(value)


def _format_latitude(value):
    if value is None:
        return ''

    return str(value)


def _format_longitude(value):
    if value is None:
        return ''

    return str(value)


def _format_hectare(value):
    if value is None:
        return ''

    return str(value)


def _format_hectare_squirrel_number(value):
    if value is None:
        return ''

    return str(value)


def _format_age(value):
    if value is None:
        return ''

    return str(value)


def _format_date(value):
    if value is None:
        return ''

    return value.strftime('%m%d%Y')


def _format_shift(value):
    if value is None:
        return ''

    return str(value)


def _format_primary_fur_color(value):
    if value is None:
        return ''

    return str(value)


def _format_highlight_fur_color(value):
    if value is None:
        return ''

    return str(value)


def _format_combination_of_primary_and_highlight_color(value):
    if value is None:
        return ''

    return str(value)


def _format_color_notes(value):
    if value is None:
        return ''

    return str(value)


def _format_location(value):
    if value is None:
        return ''

    return str(value)


def _format_specific_location(value):
    if value is None:
        return ''

    return str(value)


def _format_above_ground_sighter_measurement(value):
    if value is None:
        return ''

    return str(value)


def _format_running(value):
    if value is None:
        return ''

    return str(value)


def _format_chasing(value):
    if value is None:
        return ''

    return str(value)


def _format_climbing(value):
    if value is None:
        return ''

    return str(value)


def _format_eating(value):
    if value is None:
        return ''

    return str(value)


def _format_foraging(value):
    if value is None:
        return ''

    return str(value)


def _format_other_activities(value):
    if value is None:
        return ''

    return str(value)


def _format_kuks(value):
    if value is None:
        return ''

    return str(value)


def _format_quaas(value):
    if value is None:
        return ''

    return str(value)


def _format_moans(value):
    if value is None:
        return ''

    return str(value)


def _format_tail_flags(value):
    if value is None:
        return ''

    return str(value)


def _format_tail_twitches(value):
    if value is None:
        return ''

    return str(value)


def _format_approaches(value):
    if value is None:
        return ''

    return str(value)


def _format_indifferent(value):
    if value is None:
        return ''

    return str(value)


def _format_runs_from(value):
    if value is None:
        return ''

    return str(value)


def _format_other_interactions(value):
    if value is None:
        return ''

    return str(value)


def _format_lat_lng(value):
    if value is None:
        return ''

    return str(value)


def _format_zip_code(value):
    if value is None:
        return ''

    return str(value)


def _format_community_districts(value):
    if value is None:
        return ''

    return str(value)


def _format_borough_boundaries(value):
    if value is None:
        return ''

    return str(value)


def _format_city_council_districts(value):
    if value is None:
        return ''

    return str(value)


def _format_police_precincts(value):
    if value is None:
        return ''

    return str(value)


_FIELDS = [
    'X', 'Y', 'Unique Squirrel ID', 'Hectare', 'Shift', 'Date', 'Hectare Squirrel Number', 'Age',
    'Primary Fur Color', 'Highlight Fur Color', 'Combination of Primary and Highlight Color',
    'Color notes', 'Location', 'Above Ground Sighter Measurement', 'Specific Location', 'Running',
    'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans',
    'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from', 'Other Interactions',
    'Lat/Long', 'Zip Codes', 'Community Districts', 'Borough Boundaries', 'City Council Districts',
    'Police Precincts'
]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'dataset_location',
            nargs=1,
        )

    def handle(self, *args, **kwargs):
        path = abspath(kwargs['dataset_location'][0])

        with open(path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            dataset = Sighting.objects.all()

            num = len(dataset)
            cur = 0

            writer.writerow(_FIELDS)

            for row in dataset:  
                cur = cur + 1
                writer.writerow([
                    _format_longitude(row.longitude),
                    _format_latitude(row.latitude),
                    _format_unique_squirrel_id(row.unique_squirrel_id),
                    _format_hectare(row.hectare),
                    _format_shift(row.shift),
                    _format_date(row.date),
                    _format_hectare_squirrel_number(row.hectare_squirrel_number),
                    _format_age(row.age),
                    _format_primary_fur_color(row.primary_fur_color),
                    _format_highlight_fur_color(row.highlight_fur_color),
                    _format_combination_of_primary_and_highlight_color(row.combination_of_primary_and_highlight_color),
                    _format_color_notes(row.color_notes),
                    _format_location(row.location),
                    _format_above_ground_sighter_measurement(row.above_ground_sighter_measurement),
                    _format_specific_location(row.specific_location),
                    _format_running(row.running),
                    _format_chasing(row.chasing),
                    _format_climbing(row.climbing),
                    _format_eating(row.eating),
                    _format_foraging(row.foraging),
                    _format_other_activities(row.other_activities),
                    _format_kuks(row.kuks),
                    _format_quaas(row.quaas),
                    _format_moans(row.moans),
                    _format_tail_flags(row.tail_flags),
                    _format_tail_twitches(row.tail_twitches),
                    _format_approaches(row.approaches),
                    _format_indifferent(row.indifferent),
                    _format_runs_from(row.runs_from),
                    _format_other_interactions(row.other_interactions),
                    _format_lat_lng(row.lat_lng),
                    _format_zip_code(row.zip_code),
                    _format_community_districts(row.community_districts),
                    _format_borough_boundaries(row.borough_boundaries),
                    _format_city_council_districts(row.city_council_districts),
                    _format_police_precincts(row.police_precincts)
                ])

            print('%d of %d record(s) was exported' % (cur, num))

