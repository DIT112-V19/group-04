//
//  loginViewController.swift
//  CarInterface
//
//  Created by Kardo Dastin on 2019-05-14.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit

class loginViewController: UIViewController {
    
    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var enterButton: UIButton!
    let user = User()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    @IBAction func enterButtonPressed(_ sender: Any) {
        UserManager.shared.theUser.id = textField.text!
        print(user.id)
    }
    
    /*
     // MARK: - Navigation
     
     // In a storyboard-based application, you will often want to do a little preparation before navigation
     override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
     // Get the new view controller using segue.destination.
     // Pass the selected object to the new view controller.
     }
     */
    
}
