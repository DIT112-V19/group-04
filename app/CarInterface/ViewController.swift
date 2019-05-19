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


    @IBOutlet weak var goButton: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func goButtonPressed(_ sender: Any) {
        
        let sourceX = Int(UserManager.shared.theUser.source.x)
        let sourceY = Int(UserManager.shared.theUser.source.y)
        let destinationX = Int(UserManager.shared.theUser.destination.x)
        let destinationY = Int(UserManager.shared.theUser.destination.y)
        
        let source = [sourceX, sourceY]
        let destination = [destinationX, destinationY]
        
        let parameters = ["location": source, "destination": destination]
        
        let url = URL(string: "https://carpool.serveo.net/")!
        let session = URLSession.shared
        var request = URLRequest(url: url)
        request.httpMethod = "POST" //set http method as POST
        
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: parameters, options: .prettyPrinted)
        } catch let error {
            print(error.localizedDescription)
        }
        
        //request.addValue("multipart/form-data boundary=(boundaryConstant)", forHTTPHeaderField: "Content-Type")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        
        let task = session.dataTask(with: request as URLRequest, completionHandler: { data, response, error in
            
            guard error == nil else {
                return
            }
            guard let data = data else {
                return
            }
            do {
                if let json = try JSONSerialization.jsonObject(with: data, options: .mutableContainers) as? [String: Any] {
                    print(json)
                }
            } catch let error {
                print(error.localizedDescription)
            }
        })
        task.resume()
    }
}
