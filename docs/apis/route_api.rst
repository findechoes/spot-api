Route API
===

Document for Route API

.. http:get:: /routes

   Get all routes registered in datastore.

  ** Request e.g **

  .. sourcecode:: http

     GET /routes HTTP/1.1
     Host: navoyage.com
     Accept: application/json

  ** Response e.g **

  .. sourcecode:: http

     HTTP/1.1 200 OK
     Vary: Accept
     Content-Type: application/json

     [
       {
         "route_id": 123,
         "title": "Tokyo Bus Tour",
         "image": "http://navoyage.com/images/444.jpeg"
         "order": [
           {
             "spot_id": 456,
             "date": "YYYY-MM-DD HH:mm",
             "comment": "Good place to start a bus tour with an american style breakfast.",
             "rating": 4.5
           },
           {
             "spot_id": 345,
             "date": "YYYY-MM-DD HH:mm",
             "comment": "They view from the port resembles the beautiful coast of spain.",
             "rating": 4.0
           },
           {
             "spot_id": 444,
             "date": "YYYY-MM-DD HH:mm",
             "comment": "Lunch here is ok but not the best.",
             "rating": 3.0
           },
           {
             "spot_id": 555,
             "date": "YYYY-MM-DD HH:mm",
             "comment": "After the long road downhill, the bench here is just the place to have a rest.",
             "rating": 2.5
           }
         ]
       },
     ]
  :query sort: ``created_at`` または ``title``
  :query limit: Retrieve data count (default: 10)
  :statuscode 200: Success
  :statuscode 404: No record
