//
//  ViewController.swift
//  CarInterface
//
//  Created by Maikzy on 2019-04-02.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    private final let SERVER_URL = "https://carpool.serveo.net/"
    private final let MOVE_ENDPOINT = "move"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Tests the root endpoint of server to make sure we can access it
        sendRequest(method: "GET", endPoint: "")
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
}

