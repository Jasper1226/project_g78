import csv
from django.core.management import BaseCommand, CommandError
from os.path import abspath
from datetime import datetime
from sightings.models import Sighting


def _csv_is_null_cell(value):
    return value == ''


def _as_bool(value):
    return True if str(value).upper() == 'TRUE' else False


def _format_unique_squirrel_id(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_latitude(value):
    if _csv_is_null_cell(value):
        return None

    return float(value)


def _format_longitude(value):
    if _csv_is_null_cell(value):
        return None

    return float(value)


def _format_hectare(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_hectare_squirrel_number(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_age(value):
    if _csv_is_null_cell(value):
        return None

    return str(value).upper()


def _format_date(value):
    if _csv_is_null_cell(value):
        return None

    return datetime.strptime(value, '%m%d%Y').strftime('%Y-%m-%d')


def _format_shift(value):
    return str(value).upper()


def _format_primary_fur_color(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_highlight_fur_color(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_combination_of_primary_and_highlight_color(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_color_notes(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_location(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_specific_location(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_above_ground_sighter_measurement(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_running(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_chasing(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_climbing(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_eating(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_foraging(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_other_activities(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_kuks(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_quaas(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_moans(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_tail_flags(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_tail_twitches(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_approaches(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_indifferent(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_runs_from(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_other_interactions(value):
    if _csv_is_null_cell(value):
        return None

    return _as_bool(value)


def _format_lat_lng(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_zip_code(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_community_districts(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_borough_boundaries(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_city_council_districts(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


def _format_police_precincts(value):
    if _csv_is_null_cell(value):
        return None

    return str(value)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'dataset_location',
            nargs=1,
        )

    def handle(self, *args, **kwargs):
        path = abspath(kwargs['dataset_location'][0])

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            dataset = list(reader)

            num = len(dataset)
            cur = 0

            for row in dataset[1:]:  # For ignoring the first line
                cur = cur + 1

                longitude = _format_longitude(row[0])
                latitude = _format_latitude(row[1])
                unique_squirrel_id = _format_unique_squirrel_id(row[2])
                hectare = _format_hectare(row[3])
                shift = _format_shift(row[4])
                date = _format_date(row[5])
                hectare_squirrel_number = _format_hectare_squirrel_number(row[6])
                age = _format_age(row[7])
                primary_fur_color = _format_primary_fur_color(row[8])
                highlight_fur_color = _format_highlight_fur_color(row[9])
                combination_of_primary_and_highlight_color = _format_combination_of_primary_and_highlight_color(row[10])
                color_notes = _format_color_notes(row[11])
                location = _format_location(row[12])
                above_ground_sighter_measurement = _format_above_ground_sighter_measurement(row[13])
                specific_location = _format_specific_location(row[14])
                running = _format_running(row[15])
                chasing = _format_chasing(row[16])
                climbing = _format_climbing(row[17])
                eating = _format_eating(row[18])
                foraging = _format_foraging(row[19])
                other_activities = _format_other_activities(row[20])
                kuks = _format_kuks(row[21])
                quaas = _format_quaas(row[22])
                moans = _format_moans(row[23])
                tail_flags = _format_tail_flags(row[24])
                tail_twitches = _format_tail_twitches(row[25])
                approaches = _format_approaches(row[26])
                indifferent = _format_indifferent(row[27])
                runs_from = _format_runs_from(row[28])
                other_interactions = _format_other_interactions(row[29])
                lat_lng = _format_lat_lng(row[30])
                zip_code = _format_zip_code(row[31])
                community_districts = _format_community_districts(row[32])
                borough_boundaries = _format_borough_boundaries(row[33])
                city_council_districts = _format_city_council_districts(row[34])
                police_precincts = _format_police_precincts(row[35])

                sighting = Sighting(
                    latitude=latitude,
                    longitude=longitude,
                    unique_squirrel_id=unique_squirrel_id,
                    hectare=hectare,
                    shift=shift,
                    date=date,
                    hectare_squirrel_number=hectare_squirrel_number,
                    age=age,
                    primary_fur_color=primary_fur_color,
                    highlight_fur_color=highlight_fur_color,
                    combination_of_primary_and_highlight_color=combination_of_primary_and_highlight_color,
                    color_notes=color_notes,
                    location=location,
                    above_ground_sighter_measurement=above_ground_sighter_measurement,
                    specific_location=specific_location,
                    running=running,
                    chasing=chasing,
                    climbing=climbing,
                    eating=eating,
                    foraging=foraging,
                    other_activities=other_activities,
                    kuks=kuks,
                    quaas=quaas,
                    moans=moans,
                    tail_flags=tail_flags,
                    tail_twitches=tail_twitches,
                    approaches=approaches,
                    indifferent=indifferent,
                    runs_from=runs_from,
                    other_interactions=other_interactions,
                    lat_lng=lat_lng,
                    zip_code=zip_code,
                    community_districts=community_districts,
                    borough_boundaries=borough_boundaries,
                    city_council_districts=city_council_districts,
                    police_precincts=police_precincts
                )
                sighting.save()

                print('%d of %d record(s) was inserted' % (cur, num))

