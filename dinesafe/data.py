
from csv import DictReader
from rtree import index
from random import choice
import re

SEPARATOR = re.compile('[ -]')

class RestaurantDatabase(object):
    establishments = dict()
    tree = index.Index()
    inspections = dict()

    def __init__(self):
        pass

    def load_csv(self, fh):
        reader = DictReader(fh)

        for row in reader:
            establishment_id = long(row['establishment_id'])
            inspection_id = long(row['inspection_id'])

            if establishment_id not in self.establishments:
                establishment = dict()
                lat = float(row['lat'])
                lon = float(row['lon'])

                establishment['name'] = row['establishment_name']
                establishment['score'] = row['score']
                establishment['lat'] = lat
                establishment['lon'] = lon
                establishment['address'] = row['establishment_address']
                establishment['id'] = establishment_id
                establishment['type'] = row['establishmenttype']
                establishment['inspections'] = dict()

                self.tree.insert(establishment_id, (lat, lon, lat, lon))
                self.establishments[establishment_id] = establishment

            establishment = self.establishments[establishment_id]

            if inspection_id not in self.inspections:
                inspection = dict()
                inspection['date'] = row['inspection_date']
                inspection['infractions'] = list()
                inspection['status'] = row['establishment_status']

                establishment['inspections'][inspection_id] = inspection
                self.inspections[inspection_id] = inspection

            inspection = establishment['inspections'][inspection_id]

            if row['infraction_details']:
                infraction = dict()
                infraction['details'] = row['infraction_details']
                infraction['court_outcome'] = row['court_outcome']
                infraction['action'] = row['action']
                infraction['severity'] = row['severity']
                infraction['amount_fined'] = row['amount_fined']
                inspection['infractions'].append(infraction)

    def random(self):
        c = choice(self.establishments.keys())
        pick = self.establishments[c]
        print pick
        return pick

    def find_nearest(self, lat, lon, n):
        nearest = self.tree.nearest((lat, lon, lat, lon), n)
        return list(self.establishments[x] for x in nearest)
        
    def find_by_id(self, id):
        return self.establishments[id]

    def find_fuzzy(self, lat, lon, name):
        name = name.lower().replace("'", '')
        matches = self.tree.nearest((lat, lon, lat, lon), 100)
        top_score = None
        best_match = None
        match_set = set(SEPARATOR.split(name))
        for establishment_id in matches:
            establishment = self.establishments[establishment_id]
            test_set = set(SEPARATOR.split(establishment['name'].lower().replace("'", '')))
            score = len(match_set.intersection(test_set))
            print score, establishment['name']
            if score > top_score:
                best_match = establishment
                top_score = score
        return best_match

    def all(self):
        return self.establishments


