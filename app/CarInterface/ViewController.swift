//
//  ViewController.swift
//  CarInterface
//
//  Created by Maikzy on 2019-04-02.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation
//
//fileprivate let MERCATOR_OFFSET: Double = 268435456
//fileprivate let MERCATOR_RADIUS: Double = 85445659.44705395

class ViewController: UIViewController {


    private final let SERVER_URL = "https://carpool.serveo.net/"
    private final let MOVE_ENDPOINT = "move"
    
    
    override func viewDidLoad() {
        
        super.viewDidLoad()
        
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
