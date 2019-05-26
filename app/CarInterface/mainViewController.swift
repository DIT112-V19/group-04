//
//  mainViewController.swift
//  CarInterface
//
//  Created by Jean paul Massoud on 2019-05-11.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit

class mainViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    
    @IBOutlet weak var setButton: UIButton!
    
    var cgpoint:CGPoint?
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        UIApplication.shared.isStatusBarHidden = true
        loadImage()
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(imageTapped(tapGestureRecognizer:)))
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(tapGestureRecognizer)
        
        
    }
    override var prefersStatusBarHidden: Bool {
        return true
    }
    
    @IBAction func setButtonTapped(_ sender: Any) {
        if UserManager.shared.theUser.source != nil {
            UserManager.shared.theUser.destination = cgpoint
        }else{
            UserManager.shared.theUser.source = cgpoint
        }
    }
    
    
    @objc func imageTapped(tapGestureRecognizer: UITapGestureRecognizer){
        cgpoint = tapGestureRecognizer.location(in: imageView)
        if let bottomImage:UIImage = imageView.image {
            let topImage = locationIcon()
            imageView.image = bottomImage.imageByMergingImages(topImage: topImage, bottomImage: bottomImage)
        }
    }
    
    func locationIcon() -> UIImage{
        var im:UIImage?
        if let image = UIImage(named: "address.png"){
            im = resizeImage(image: image)
        }
        return im!
    }
    
    func resizeImage(image: UIImage) -> UIImage? {
        
        //let scale = newWidth / image.size.width
        //let newHeight = image.size.height * scale
        // print("image size ", image.size)
        UIGraphicsBeginImageContext(CGSize(width: image.size.width, height: image.size.height))
        image.draw(in: CGRect(x: cgpoint!.x, y: cgpoint!.y/2, width: 12, height: 12))
        
        let newImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        
        return newImage
    }
    
    
    func loadImage(){
        
        let size = UIScreen.main.bounds.size
        if let image = UIImage(named:"map (1).png") {
            let finalImage = image.scaleTo(with: size)
            self.imageView.image = finalImage
            
        }
    }
    
    
    
}

extension UIImage {
    
    func scaleTo(with size: CGSize) -> UIImage? {
        var scaledImageRect = CGRect.zero
        
        let aspectWidth:CGFloat = size.width / self.size.width
        let aspectHeight:CGFloat = size.height / self.size.height
        let aspectRatio:CGFloat = min(aspectWidth, aspectHeight)
        
        scaledImageRect.size.width = self.size.width * aspectRatio
        scaledImageRect.size.height = self.size.height * aspectRatio
        scaledImageRect.origin.x = (size.width - scaledImageRect.size.width) / 2.0
        scaledImageRect.origin.y = (size.height - scaledImageRect.size.height) / 2.0
        
        UIGraphicsBeginImageContextWithOptions(size, false, 0)
        
        self.draw(in: scaledImageRect)
        
        let scaledImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        
        return scaledImage
    }
    
    //    func resizeImage(targetSize: CGSize) -> UIImage {
    //        let size = self.size
    //        let widthRatio  = targetSize.width  / size.width
    //        let heightRatio = targetSize.height / size.height
    //        let newSize = widthRatio > heightRatio ?  CGSize(width: size.width * heightRatio, height: size.height * heightRatio) : CGSize(width: size.width / widthRatio,  height: size.height / widthRatio)
    //        let rect = CGRect(x: 0, y: 0, width: newSize.width, height: newSize.height)
    //
    //        UIGraphicsBeginImageContextWithOptions(newSize, false, 1.0)
    //        self.draw(in: rect)
    //        let newImage = UIGraphicsGetImageFromCurrentImageContext()
    //        UIGraphicsEndImageContext()
    //
    //        return newImage!
    //    }
    //
    func imageByMergingImages(topImage: UIImage, bottomImage: UIImage, scaleForTop: CGFloat = 1.0) -> UIImage {
        let size = bottomImage.size
        let container = CGRect(x: 0, y: 0, width: size.width, height: size.height)
        UIGraphicsBeginImageContextWithOptions(size, false, 1.0)
        UIGraphicsGetCurrentContext()!.interpolationQuality = .high
        bottomImage.draw(in: container)
        
        let topWidth = size.width / scaleForTop
        let topHeight = size.height / scaleForTop
        let topX = (size.width / 2.0) - (topWidth / 2.0)
        let topY = (size.height / 2.0) - (topHeight / 2.0)
        
        topImage.draw(in: CGRect(x: topX, y: topY, width: topWidth, height: topHeight), blendMode: .normal, alpha: 1.0)
        
        return UIGraphicsGetImageFromCurrentImageContext()!
    }
    
}


