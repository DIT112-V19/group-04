# Carpool API documentation
**Base url:** http://carpool.serveo.net/api/


### Endpoints

#### /pickup [POST]

###### Headers
* Cookie = id=value (values = ['bartek', 'alex', 'konrad', 'kalle, 'kardo', 'jean'])
* Content-Type = 'application/json'

###### Example payload
    {
        location: [20, 40],
        destination: [30, 50]
    }
 
