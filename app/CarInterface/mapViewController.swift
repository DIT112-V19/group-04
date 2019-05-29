//
//  mainViewController.swift
//  CarInterface
//
//  Created by Jean paul Massoud on 2019-05-11.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit

class mapViewController: UIViewController {
    
    //UI elements
    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var setButton: UIButton!
    //Attributes
    let imageCache = ImageCache.shared
    let tools = Tools.shared
    var cgpoint:CGPoint?
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        UIApplication.shared.isStatusBarHidden = true //TODO: replace this method call
        imageView.image = loadMapImage()
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(imageTapped(tapGestureRecognizer:)))
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(tapGestureRecognizer)
        
        
    }
    
    //Assign the the values from the user tap into user object as source/destiation
    @IBAction func setButtonTapped(_ sender: Any) {
        if UserManager.shared.theUser.source != nil {
            UserManager.shared.theUser.destination = self.cgpoint!
        }else{
            UserManager.shared.theUser.source = self.cgpoint!
        }
    }
    
    // draw address icon on image accourding to user tap
    @objc func imageTapped(tapGestureRecognizer: UITapGestureRecognizer){
        cgpoint = tapGestureRecognizer.location(in: imageView)
        let bottomImage = loadMapImage()
        let topImage = addressIcon()
        let point = CGPoint(x: cgpoint!.x, y: cgpoint!.y-25)
        DispatchQueue.main.async {
            self.imageView.image = self.tools.imageByMergingImages(topImage: topImage,
                                                              bottomImage: bottomImage,
                                                              topImgLoc: point,
                                                              scaleForTop: 12)
        }
        
    }
    // load images from cache
    func addressIcon() -> UIImage{
     return  imageCache.getAddressImage()
    }
    func loadMapImage()-> UIImage{
        let size = UIScreen.main.bounds.size
        let image = imageCache.getMapImage()
        return tools.scaleTo(size: size, image: image)!
    }
    
    
    
}


