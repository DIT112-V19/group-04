//
//  ViewController.swift
//  CarInterface
//
//  Created by Maikzy on 2019-04-02.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation

class ViewController: UIViewController {

    @IBOutlet weak var rButton: UIButton!
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var mapView: MKMapView!
    private final let SERVER_URL = "https://carpool.serveo.net/"
    private final let MOVE_ENDPOINT = "move"
    let locationManager = CLLocationManager()
    let regionInMeters: Double = 1000
    var directionsArray: [MKDirections] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        checkLocationServices()
        
        // Tests the root endpoint of server to make sure we can access it
        sendRequest(method: "GET", endPoint: "")
    }

    @IBAction func rButtonTapped(_ sender: Any) {
        initLindHolmenMap()
    }
    @IBAction func forward(_ sender: Any) {
        sendRequest(method: "GET", endPoint: MOVE_ENDPOINT)
    }
    
    private func sendRequest(method: String, endPoint: String) {
        let url = URL(string: SERVER_URL + endPoint)
        
        let task = URLSession.shared.dataTask(with: url!) { (data, res, er) in
            if let data = data {
                print(data.description)
            }
        }
        task.resume()
    }
    
   
    
    func checkLocationServices() {
        if CLLocationManager.locationServicesEnabled() {
            setupLocationManager()
            checkLocationAuthorization()
        } else {
            // Show alert letting the user know they have to turn this on.
        }
    }
    
    func setupLocationManager() {
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
    }
    
    func checkLocationAuthorization() {
        switch CLLocationManager.authorizationStatus() {
        case .authorizedWhenInUse:
            locationManager.requestAlwaysAuthorization()
            
        case .denied:
            locationManager.requestAlwaysAuthorization()
            
        case .notDetermined:
            locationManager.requestAlwaysAuthorization()
            
        case .restricted:
            locationManager.requestAlwaysAuthorization()
            
        case .authorizedAlways:
            initLindHolmenMap()
            showCompass()
            showTrackingButton()
            break
        }
    }
    
    
    func showCompass() {
        mapView.showsCompass = false
        let comapssButton = MKCompassButton(mapView:mapView)
        comapssButton.compassVisibility = .visible
        mapView.addSubview(comapssButton)
        
        comapssButton.translatesAutoresizingMaskIntoConstraints = false
        comapssButton.leftAnchor.constraint(equalTo: mapView.leftAnchor, constant: 15).isActive = true
        comapssButton.topAnchor.constraint(equalTo: mapView.topAnchor, constant: 25).isActive = true
        
    }
    
    func showTrackingButton() {
        let userTrackingButton = MKUserTrackingButton(mapView: mapView)
        mapView.addSubview(userTrackingButton)
        userTrackingButton.translatesAutoresizingMaskIntoConstraints = false
        userTrackingButton.rightAnchor.constraint(equalTo: mapView.rightAnchor, constant: -5).isActive = true
        userTrackingButton.topAnchor.constraint(equalTo: mapView.topAnchor, constant: 25).isActive = true
        
        
    }
    
    
    
    func initLindHolmenMap(){
        let lindHolmenLoc = CLLocation(latitude: 57.708604, longitude: 11.938750)
        let regionRadius = CLLocationDistance(exactly: 1000)!
        let linHolmenRegion = MKCoordinateRegion(center:lindHolmenLoc.coordinate, latitudinalMeters: regionRadius
                , longitudinalMeters: regionRadius)
        let edgeInsets = UIEdgeInsets(top: 15, left: 15, bottom: 15, right: 15);
        mapView.setVisibleMapRect(MKMapRectForCoordinateRegion(region: linHolmenRegion), edgePadding: edgeInsets, animated: true)
        
        mapView.isScrollEnabled = false
        mapView.isZoomEnabled = false
        mapView.isRotateEnabled = false
    }
    
    
    func MKMapRectForCoordinateRegion(region:MKCoordinateRegion) -> MKMapRect {
        let topLeft = CLLocationCoordinate2D(latitude: region.center.latitude + (region.span.latitudeDelta/2), longitude: region.center.longitude - (region.span.longitudeDelta/2))
        let bottomRight = CLLocationCoordinate2D(latitude: region.center.latitude - (region.span.latitudeDelta/2), longitude: region.center.longitude + (region.span.longitudeDelta/2))
        
        let a = MKMapPoint(topLeft)
        let b = MKMapPoint(bottomRight)
        
        return MKMapRect(origin: MKMapPoint(x:min(a.x,b.x), y:min(a.y,b.y)), size: MKMapSize(width: abs(a.x-b.x), height: abs(a.y-b.y)))
    }
    
    
}


extension ViewController: CLLocationManagerDelegate {
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else { return }
        let region = MKCoordinateRegion.init(center: location.coordinate, latitudinalMeters: regionInMeters, longitudinalMeters: regionInMeters)
        mapView.setRegion(region, animated: true)
    }
    
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        checkLocationAuthorization()
    }
    
}

extension MKCoordinateRegion{
    var mapRect:MKMapRect {
        get{
            let a = MKMapPoint(CLLocationCoordinate2DMake(
                self.center.latitude + self.span.latitudeDelta / 2,
                self.center.longitude - self.span.longitudeDelta / 2))
            
            let b = MKMapPoint(CLLocationCoordinate2DMake(
                self.center.latitude - self.span.latitudeDelta / 2,
                self.center.longitude + self.span.longitudeDelta / 2))
            
            return MKMapRect(x: min(a.x,b.x), y: min(a.y,b.y), width: abs(a.x-b.x), height: abs(a.y-b.y))
        }
    }
}

extension MKMapView {
    func setVisibleRegion(mapRegion: MKCoordinateRegion, edgePadding insets: UIEdgeInsets, animated animate: Bool) {
        self.setVisibleMapRect(mapRegion.mapRect, edgePadding: insets , animated: animate)
    }
}
