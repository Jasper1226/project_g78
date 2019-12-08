from squirrel import models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('dataset_path', nargs=1)

    def handle(self, *args, **kwargs):
        def format_date(x):
            return datetime.strptime(x, '%m%d%Y').strftime('%Y-%m-%d')

        def format_agsm(x):
            return -1 if x == 'FALSE' else None if x == '' else x

        def format_bool(x):
            return True if x == 'TRUE' else False

        path = abspath(kwargs['dataset_path'][0])

        if not isfile(path):
            print('invalid dataset path', file=sys.stderr)
            return

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            dataset = list(reader)

            num = len(dataset)
            cur = 0
            is_first_line = True

            print('%d row(s) will be processed' % num)

            for row in dataset:

                if is_first_line:
                    is_first_line = False
                    continue

                cur = cur + 1
                models.Sighting.objects.create(x=row[0], y=row[1], uniqueSquirrelId=row[2], hectare=row[3],
                                               shift=row[4],
                                               date=format_date(row[5]),
                                               hectareSquirrelNumber=row[6], age=row[7],
                                               primaryFurColor=row[8], highlightFurColor=row[9],
                                               combinationOfPrimaryAndHighlightColor=row[10], colorNotes=row[11],
                                               location=row[12], aboveGroundSighterMeasurement=format_agsm(row[13]),
                                               specificLocation=row[14], running=format_bool(row[15]),
                                               chasing=format_bool(row[16]), climbing=format_bool(row[17]),
                                               eating=format_bool(row[18]), foraging=format_bool(row[19]),
                                               otherActivities=row[20], kuks=format_bool(row[21]),
                                               quaas=format_bool(row[22]), moans=format_bool(row[23]),
                                               tailFlags=format_bool(row[24]), tailTwitches=format_bool(row[25]),
                                               approaches=format_bool(row[26]), indifferent=format_bool(row[27]),
                                               runsFrom=format_bool(row[28]),
                                               otherInteractions=row[29], textOfLatAndLng=row[30], zipCodes=row[31],
                                               communityDistricts=row[32], boroughBoundaries=row[33],
                                               cityCouncilDistricts=row[34], policePrecincts=row[35])
                print('%d of %d record(s) was inserted' % (cur, num))

            print('done')

