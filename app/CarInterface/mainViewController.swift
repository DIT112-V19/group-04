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
    
    
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        loadImage()
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(imageTapped(tapGestureRecognizer:)))
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(tapGestureRecognizer)

       
    }
    
    @IBAction func setButtonTapped(_ sender: Any) {
    }
    
    
    @objc func imageTapped(tapGestureRecognizer: UITapGestureRecognizer){
        let cgpoint = tapGestureRecognizer.location(in: imageView)
        
        //        cgpoint.x = cgpoint.x / imageView.bounds.width
        //        cgpoint.y = cgpoint.y / imageView.bounds.height
        debugPrint(cgpoint)
    }
    
    func loadImage(){
        
        let size = imageView.bounds.size
        if let image = UIImage(named:"map (1).png") {
            let finalImage = image.scaleTo(with: size)
            self.imageView.image = image
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
}
