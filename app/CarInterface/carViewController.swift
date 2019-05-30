//
//  carViewController.swift
//  CarInterface
//
//  Created by Jean paul Massoud on 2019-05-29.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit
import Foundation



class carViewController: UIViewController {
    
    //UI elements
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var backButton: UIButton!
    
    //Attributes
    var timer :Timer?
    let updateRatio: Double = 3 //seconds
    var car = carManager.shared
    var user = UserManager.shared
    let cache = ImageCache.shared
    let tools = Tools.shared
    let connection = httpManager.shared
    var image : UIImage?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.imageView.image = loadMapWithMarks()
        if car.theCar.location != nil{
            printCar(point: car.theCar.location)
        }
        startScheduling(seconds: self.updateRatio)
    }
    
    // back button ; it stops the get calls
    @IBAction func backButtonPressed(_ sender: Any) {
        stopScheduling()
    }
    
    // scheduling method calls by seconds
    func startScheduling(seconds:Double){
        if timer == nil{
            timer = Timer.scheduledTimer(timeInterval: seconds,
                                         target: self,
                                         selector: #selector(self.getCarLocation),
                                         userInfo: nil,
                                         repeats: true)
        }
        
    }
    // stop the method calls
    func stopScheduling(){
        if timer != nil {
            timer!.invalidate()
            timer = nil
        }
    }
    
    //This method is scheduled in viewDidLoad to be called as long as the view is active
    @objc func getCarLocation(){
        connection.updateCarLocation()
        self.printCar(point: car.theCar.location)
       
    }
    // Print car on the image according to its location
    func printCar(point:CGPoint){
        var image = UIImage()
        let bottomImage = loadMapWithMarks()
        let topImage = cache.getCarImage()
        image = tools.imageByMergingImages(topImage: topImage, bottomImage: bottomImage,topImgLoc: point, scaleForTop: 12)
        DispatchQueue.main.async {
            self.imageView.image = image
        }
    }
    
    // Generate an image containing source/destination annotations on map image
    func loadMapWithMarks()-> UIImage{
        if self.image == nil {
            var img = UIImage()
            var image = UIImage()
            let map = loadMapImage()
            let address = cache.getAddressImage()
            let src =  user.theUser.source
            let dst =  user.theUser.destination
            let source = CGPoint(x: src!.x, y: src!.y - 25)
            let destination = CGPoint(x: dst!.x, y: dst!.y - 25)
            img = tools.imageByMergingImages(topImage: address, bottomImage: map, topImgLoc: source, scaleForTop: 12)
            image = tools.imageByMergingImages(topImage: address, bottomImage: img, topImgLoc: destination, scaleForTop: 12)
            
            return image
        }else{ return self.image! }
    }
    
    // loading from image cache as well as scaling the image
    func loadMapImage()-> UIImage{
        let size = UIScreen.main.bounds.size
        let image = self.cache.getMapImage()
        return tools.scaleTo(size: size,image: image)!
    }
    
    
    
    
    
    
   
    
}

