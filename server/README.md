# Carpool API documentation
**Base url:** http://carpool.serveo.net/api/


### Endpoints

#### /pickup [POST]

###### Headers
* Cookie: id=value | e.g. id=bartek
* Content-Type: 'application/json'

###### Example payload
    {
        location: [20, 40],
        destination: [30, 50]
    }
 
###### Example response
    {
        carLocation: [
            230,
            800
        ]
    }
    
 #### /getlocation [GET]

###### Headers
* Cookie: id=value | e.g. id=bartek
* Content-Type: 'application/json'

Note that this only works if the customer is a valid passenger.


###### Example response
    {
        carLocation: [
            230,
            800
        ]
    }
 
