//
//  Tools.swift
//  CarInterface
//
//  Created by Jean paul Massoud on 2019-05-29.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import Foundation
import UIKit

class Tools {
    static let shared = Tools()
    init() {}
    
    //Attributes
    let screenWidth = UIScreen.main.bounds.width
    let screenHeight = UIScreen.main.bounds.height
    
    // convert the coordinates retrieved from server
    func deConverter(location: CGPoint) -> CGPoint{
        let locationX = Int((location.x / 1557) * screenWidth)
        let locationY = Int((location.y / 2768) * screenHeight)
        
        return CGPoint(x: locationY, y: locationX)
    }
    // convert the coordinates before sending them to server
    func converter(location:CGPoint) -> CGPoint{
        let sX = (location.x/screenWidth) * 1557
        let sY = (location.y/screenHeight) * 2768
        
        return CGPoint(x: Int(sY), y: Int(sX))
    }
    // Generate array from a CGPoint
    func toArray (point:CGPoint) -> [Int] {
        var arr:[Int] = .init()
        let x = point.x
        let y = point.y
        arr.append(Int(x))
        arr.append(Int(y))
        return arr
    }
    // Scale an image to fit a size
    func scaleTo(size: CGSize, image: UIImage) -> UIImage? {
        var scaledImageRect = CGRect.zero
        
        let aspectWidth:CGFloat = size.width / image.size.width
        let aspectHeight:CGFloat = size.height / image.size.height
        let aspectRatio:CGFloat = min(aspectWidth, aspectHeight)
        
        scaledImageRect.size.width = image.size.width * aspectRatio
        scaledImageRect.size.height = image.size.height * aspectRatio
        scaledImageRect.origin.x = (size.width - scaledImageRect.size.width) / 2.0
        scaledImageRect.origin.y = (size.height - scaledImageRect.size.height) / 2.0
        
        UIGraphicsBeginImageContextWithOptions(size, false, 0)
        
        image.draw(in: scaledImageRect)
        
        let scaledImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        
        return scaledImage
    }
    // Merge two images; draw one up on the other. 
    func imageByMergingImages(topImage: UIImage, bottomImage: UIImage,topImgLoc:CGPoint, scaleForTop: CGFloat = 1.0) -> UIImage {
        let size = bottomImage.size
        let container = CGRect(x: 0, y: 0, width: size.width, height: size.height)
        UIGraphicsBeginImageContextWithOptions(size, false, 1.0)
        UIGraphicsGetCurrentContext()!.interpolationQuality = .high
        bottomImage.draw(in: container)
        
        let topWidth = size.width / scaleForTop
        let topHeight = size.height / scaleForTop
        let topX = topImgLoc.x
        let topY = topImgLoc.y
        
        topImage.draw(in: CGRect(x: topX, y: topY, width: topWidth, height: topHeight), blendMode: .normal, alpha: 1.0)
        
        return UIGraphicsGetImageFromCurrentImageContext()!
    }
    
}
