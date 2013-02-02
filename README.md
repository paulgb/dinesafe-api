DineSafe API Server
===================

A simple API to access DineSafe data. In addition to the data published by DineSafe, the results include the geocoded coordinates of the address and a point score assigned based on recent infractions.

Calls
-----

## Establishment Information

    http://[base_url]/establishment?id=[establishment_id]

Return the data on a specific establishment.

### Example

    http://[base_url]/establishment?id=9013708

    {
        name: "SECOND CUP",
        lon: -79.3716892,
        score: "100",
        address: "163 KING ST E",
        lat: 43.6504456,
        inspections: {
            102475629: {
                date: "2011-03-10",
                infractions: [ ],
                status: "Pass"
            },
            102692460: {
                date: "2012-02-09",
                infractions: [ ],
                status: "Pass"
            }
        },
        type: "Restaurant",
        id: 9013708
    }

## Random Establishment

    http://[base_url]/random

Return the data on a random establishment.

### Example

    http://[base_url]/random

    {
        name: "TAH DEEG",
        lon: -79.4149499,
        score: "100",
        address: "5525 YONGE ST",
        lat: 43.7784115,
        inspections: {
            102492978: {
                date: "2011-03-24",
                infractions: [
                    {
                        action: "Notice to Comply",
                        severity: "S - Significant",
                        amount_fined: "NA",
                        details: "Operator fail to provide easily readable thermometer(s)",
                        court_outcome: ""
                    },
                    {
                        action: "Notice to Comply",
                        severity: "S - Significant",
                        amount_fined: "NA",
                        details: "Operator fail to provide separate handwashing sink(s)",
                        court_outcome: ""
                    },
                    {
                        action: "Notice to Comply",
                        severity: "NA - Not Applicable",
                        amount_fined: "NA",
                        details: "Fail to post the eating and drinking establishment license adjacent to the food safety inspection notice - Municipal Code Chapter 545 Sec. 5G(4)",
                        court_outcome: ""
                    },
                    {
                        action: "Notice to Comply",
                        severity: "S - Significant",
                        amount_fined: "NA",
                        details: "Operator fail to provide required supplies at sinks",
                        court_outcome: ""
                    }
                ],
                status: "Conditional Pass"
            },
            102493047: {
                date: "2011-04-01",
                infractions: [ ],
                status: "Pass"
            },
            102574840: {
                date: "2011-08-09",
                infractions: [ ],
                status: "Pass"
            },
            102639764: {
                date: "2011-11-24",
                infractions: [ ],
                status: "Pass"
            },
            102702985: {
                date: "2012-02-27",
                infractions: [ ],
                status: "Pass"
            },
            102775111: {
                date: "2012-06-25",
                infractions: [ ],
                status: "Pass"
            },
            102878032: {
                date: "2012-12-18",
                infractions: [ ],
                status: "Pass"
            }
        },
        type: "Food Take Out",
        id: 10397287
    } 


