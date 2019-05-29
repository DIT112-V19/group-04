//
//  ImageCache.swift
//  CarInterface
//
//  Created by Jean paul Massoud on 2019-05-29.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import Foundation
import UIKit

class ImageCache {
    
    static let shared = ImageCache()
    let cache = NSCache<AnyObject, AnyObject>()
    let size = CGSize(width: 316, height: 171)
    init(){}
    
   
    //we call this function whenever to retrieve a car icon
    func getCarImage () -> UIImage{
        var img = UIImage()
        if  let imageFromCache = cache.object(forKey: "car" as AnyObject) as? UIImage {
            img = imageFromCache
        }
        else {
            setter(name: "car")
            img = getCarImage()
        }
        return img
    }
    //we call this function whenever to retrieve the map image
    func getMapImage () -> UIImage{
        var img = UIImage()
        if  let imageFromCache = cache.object(forKey: "map" as AnyObject) as? UIImage {
            img = imageFromCache
        }
        else {
            setter(name: "map")
            img = getMapImage()
        }
        return img
    }
    //we call this function whenever to retrieve a address icon
    func getAddressImage () -> UIImage{
        var img = UIImage()
        if  let imageFromCache = cache.object(forKey: "address" as AnyObject) as? UIImage {
            img = imageFromCache
        }
        else {
            setter(name: "address")
            img = getAddressImage()
        }
        return img
    }
    
    
    //we call this function to load an image to cache object
    func setter(name:String){
            let image = UIImage()
            let imageToCache = image.load(image: name)
            self.cache.setObject(imageToCache, forKey: name as AnyObject)
        }
    // we call this method once to...
    func saveEmAll() {
        setter(name: "car")
        setter(name: "map")
        setter(name: "address")
    }
    
    
  
}

extension UIImage {
    
    func load(image imageName: String) -> UIImage {
        // declare image location
        let imagePath: String = "\(NSSearchPathForDirectoriesInDomains(.documentDirectory, .userDomainMask, true)[0])/\(imageName).png"
        let imageUrl: URL = URL(fileURLWithPath: imagePath)
        
        // check if the image is stored already
        if FileManager.default.fileExists(atPath: imagePath),
            let imageData: Data = try? Data(contentsOf: imageUrl),
            let image: UIImage = UIImage(data: imageData, scale: UIScreen.main.scale) {
            return image
        }
        
        // image has not been created yet: create it, store it, return it
        let newImage = UIImage(named:"\(imageName)")
        try? newImage!.pngData()?.write(to: imageUrl)
        return newImage!
    }
}
