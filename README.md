# group-04

## What?
This project is intended as a proof of concept for a car pooling service. 

It has a server that runs the service itself.
It has the capability to run either arduino smartcars, simulated vehicles or a combination of both. 
The project also contains an app that is used for ordering a transportation.
## Why?
If this would be implemented as a future service using autonomous vehicles it is our belief that this could help solve the problem with congestion.

We believe that using this as public transportation would be a faster alternative than what's currently available on the market.
This could potentially reduce the number of vehicles needed as some individuals, who do not currently use public transportation, might be convinced to use this service
as the availability and speed of this service would hopefully be greater than today's alternatives.

## How?
The arduino prototype vehicle is based on the Smartcar shield platform which can be viewed here.
* [The Smartcar platform](http://plat.is/smartcar)

The server and  it's additional features is written in python.

## Requirements
To be able to run the server you need the following:

* Python 3 or newer
* Virtualenv

`virtualenv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

In order to temporarily forward your port and make it accessible for other devices, we can use <a href="https://serveo.net/"> this service </a>:

`ssh -R carpool:80:localhost:5000 serveo.net`

The service itself also requires a graph of a map.
You can either use the one provided with the server, or you can create your own using the mapcreator in the server/utils/mapcreator folder. 

## Software:
* Android Studio
* Arduino IDE 
