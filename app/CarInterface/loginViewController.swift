//
//  loginViewController.swift
//  CarInterface
//
//  Created by Kardo Dastin on 2019-05-14.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit

class loginViewController: UIViewController {
    
    // UI elements
    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var enterButton: UIButton!

    
    override func viewDidLoad() {
        super.viewDidLoad()
        ImageCache.shared.saveEmAll()
    }
    
    // Assign the input text to the user object
    @IBAction func enterButtonPressed(_ sender: Any) {
        UserManager.shared.theUser.id = textField.text!
        print(UserManager.shared.theUser.id)
    }
    
}
