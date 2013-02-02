
from csv import DictReader
from rtree import index

class RestaurantDatabase(object):
    establishments = dict()
    tree = index.Index()
    inspections = dict()

    def __init__(self, fh):
        reader = DictReader(fh)

        for row in reader:
            establishment_id = long(row['establishment_id'])
            inspection_id = long(row['inspection_id'])

            if establishment_id not in self.establishments:
                establishment = dict()
                lat = float(row['lat'])
                lon = float(row['lon'])

                establishment['lat'] = lat
                establishment['lon'] = lon
                establishment['address'] = row['establishment_address']
                establishment['id'] = establishment_id
                establishment['type'] = row['establishmenttype']
                establishment['status'] = row['establishment_status']
                establishment['inspections'] = dict()

                self.tree.insert(establishment_id, (lat, lon, lat, lon), establishment)
                self.establishments[establishment_id] = establishment

            establishment = self.establishments[establishment_id]

            if inspection_id not in self.inspections:
                inspection = dict()
                inspection['date'] = row['inspection_date']
                inspection['infractions'] = list()

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

    def find_nearest(self, lat, lon):
        pass


