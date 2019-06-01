# group-04

## What?
This project is intended as a proof of concept for a car pooling service. 

It has a server that runs the service itself.
It has the capability to run either arduino smartcars, simulated vehicles or a combination of both. 
The project also contains an app that is used for ordering a transportation.
## Why?
If this would be implemented as a future service using autonomous vehicles it is our belief that this could help solve the problem with congestion while at the same time providing a more ecological and economic solution than the 'one vehicle, one person' approach of the 20th century.

We believe that using this as public transportation would be a faster alternative than what's currently available on the market.
This could potentially reduce the number of vehicles needed as some individuals, who do not currently use public transportation, might be convinced to use this service
as the availability and speed of this service would hopefully be greater than today's alternatives.

We also believe that this form of car pooling service can greatly reduce the amount of space required for car parking thereby allowing the city of the 21st century to turn parking lots back into public green spaces. As a user you'd never again look for a parking lot, will never have to worry about bringing a car to the workshop for maintenance or repairs and will never again forget the keys. As a society this form of car sharing can greatly reduce the amount of cars needed as currently most cars a parked for most of their life.

## Video Demo

Please follow this link to view our final product demonstration on YouTube.
[Click here for a free virus!](https://youtu.be/HYsL9aRIo1g)

## How?
The arduino prototype vehicle is based on the Smartcar shield platform which can be viewed here.
* [The Smartcar platform](http://plat.is/smartcar)

The server and  it's additional features is written in python.
The IOS client is written in Swift.


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

To be able to run the server you need the following:

* Python 3 or newer
* Virtualenv

To be able to run the IOS app you need the following:

* Xcode (simulator)
* Apple iPhone - iOS 11.0 (or above)
* Developer apple id (free dev-account work as well)

To be able to flash the arduino script onto the microcontroller you need the following:
* Arduino Studio
* Link cable

Connect the microcontroller to your pc running arduino studio, select the used port and press on the flash-button.

Once the microcontroller is running our arduino sketch, just turn on the power and connect your PC to the microcontroller using bluetooth. 

## IOS Application

* Import Xcode project.
* Choose a device or simulator to build and run the Application.
* Create a username and press login.
* Tap on source to insert the location where you desire the car to pick you up. Once that's done, tap on SET.
* Tap on destination to insert the location where you desire the car to drop you. Once that's done, tap on SET.
* Finally, tap 'GO' to get a visualisation of your location, destination, as well as the vihicle which is on the way.
