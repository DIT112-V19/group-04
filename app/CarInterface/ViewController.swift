//
//  ViewController.swift
//  CarInterface
//
//  Created by Maikzy on 2019-04-02.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit
import CoreLocation

class ViewController: UIViewController {
    
    @IBOutlet weak var goButton: UIButton!
    let connection = httpManager.shared
    let car = carManager.shared
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    // send a post request and assign the response to the car object
    @IBAction func goButtonPressed(_ sender: Any) {
        self.connection.postContent()
    }
    
    
}
