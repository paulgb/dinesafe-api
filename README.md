DineSafe API Server
===================

A simple API to access DineSafe data. In addition to the data published by Toronto Public Health's [DineSafe](http://www.toronto.ca/health/dinesafe/index.htm), the results include the geocoded coordinates of the address and a point score assigned based on recent infractions. The server loads the data into an in-memory R-Tree to provide efficient location queries.

Calls
-----

### Establishment Information

    http://[base_url]/establishment?id=[establishment_id]

Return the data on a specific establishment.

#### Example Request

    http://[base_url]/establishment?id=9013708

#### Example Response

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

### Random Establishment

    http://[base_url]/random

Return the data on a random establishment.

#### Example Request

    http://[base_url]/random

#### Example Response

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

### Establishments Near Location

    http://[base_url]/near?lat=[latitude]&lon=[longitude]&n=[num_results]

Return the _n_ nearest results to a given coordinate. _n_ defaults to 10.

#### Example Request

    /near?lat=-79.2653504&lon=43.7712337&n=2

#### Example Response

    [
        {
            name: "SUBWAY",
            lon: -79.1367173,
            score: "100",
            address: "5550 LAWRENCE AVE E",
            lat: 43.7795895,
            inspections: {
                102392547: {
                    date: "2011-02-28",
                    infractions: [ ],
                    status: "Pass"
                },
                102614413: {
                    date: "2011-10-12",
                    infractions: [ ],
                    status: "Pass"
                },
                102846127: {
                    date: "2012-10-23",
                    infractions: [ ],
                    status: "Pass"
                }
            },
            type: "Restaurant",
            id: 10287417
        },
        {
            name: "MR BEAN COFFEE CO",
            lon: -79.1367173,
            score: "100",
            address: "5550 LAWRENCE AVE E",
            lat: 43.7795895,
            inspections: {
                102392522: {
                    date: "2011-02-28",
                    infractions: [ ],
                    status: "Pass"
                },
                102614391: {
                    date: "2011-10-12",
                    infractions: [ ],
                    status: "Pass"
                },
                102846145: {
                    date: "2012-10-23",
                    infractions: [ ],
                    status: "Pass"
                }
            },
            type: "Restaurant",
            id: 10317653
        }
    ]

### Fuzzy Match

    http://[base_url]/fuzzy_match?lat=[latitude]&lon=[longitude]&name=[name]

Match an establishment near a coordinate with a given (possibly inexact) name.

#### Example Request

    http://[base_url]/fuzzy_match?lat=-79.2653504&lon=43.7712337&name=bean

#### Example Response

    {
        name: "MR BEAN COFFEE CO",
        lon: -79.1367173,
        score: "100",
        address: "5550 LAWRENCE AVE E",
        lat: 43.7795895,
        inspections: {
            102392522: {
                date: "2011-02-28",
                infractions: [ ],
                status: "Pass"
            },
            102614391: {
                date: "2011-10-12",
                infractions: [ ],
                status: "Pass"
            },
            102846145: {
                date: "2012-10-23",
                infractions: [ ],
                status: "Pass"
            }
        },
        type: "Restaurant",
        id: 10317653
    }

