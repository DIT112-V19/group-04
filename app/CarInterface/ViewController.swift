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
    var source = [Int]()
    var destination = [Int]()
    var userId = ""
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    func convert() -> Void {
        
        let screenSize = UIScreen.main.bounds
        let screenWidth = screenSize.width
        let screenHeight = screenSize.height
        
        
        let sX = (UserManager.shared.theUser.source.x/screenWidth) * 1557
        let sY = (UserManager.shared.theUser.source.y/screenHeight) * 2768
        let dX = (UserManager.shared.theUser.destination.x/screenWidth) * 1557
        let dY = (UserManager.shared.theUser.destination.y/screenHeight) * 2768
        
        
        let sourceX = Int(sX)
        let sourceY = Int(sY)
        let destinationX = Int(dX)
        let destinationY = Int(dY)
        
        
        self.source = [sourceX, sourceY]
        self.destination = [destinationX, destinationY]
        self.userId = UserManager.shared.theUser.id
    }
    
    func sendRequest() {
        
         print("POST")
        
        
        let param = ["location": source, "destination": destination]
        
        
        
        // create post request
        let url = URL(string: "http://127.0.0.1:5000/api/pickup")!
        
        let parameters = ["location": source, "destination": destination]
        let session = URLSession.shared
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        
        
        let jar = HTTPCookieStorage.shared
        let cookieHeaderField = ["Cookie": userId]
        let cookies = HTTPCookie.cookies(withResponseHeaderFields: cookieHeaderField, for: url)
        jar.setCookies(cookies, for: url, mainDocumentURL: url)
        
        
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: parameters, options: .prettyPrinted)
        } catch let error {
            print(error.localizedDescription)
        }
        
        debugPrint("hey")
        
        debugPrint(parameters)
        debugPrint(cookieHeaderField)
        
        
        
        //request.addValue("multipart/form-data boundary=(boundaryConstant)", forHTTPHeaderField: "Content-Type")
        request.addValue("application/json", forHTTPHeaderField: userId)
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
        self.getInfo()
    }
    
    func getInfo(){
        
        print("GET")
        
        guard let url = URL(string: "https://levamen.serveo.net/api/pickup") else { return }
        
        let session = URLSession.shared
        session.dataTask(with: url) { (data, response, error) in
            if let response = response {
                print(response)
            }
            
            if let data = data {
                print(data)
                do {
                    let json = try JSONSerialization.jsonObject(with: data, options: [])
                    print(json)
                } catch {
                    print(error)
                }
                
            }
            }.resume()
        print("DONE")
    }
    

    @IBAction func goButtonPressed(_ sender: Any) {
        self.convert()
        self.sendRequest()
    }
    
}
//extension Dictionary {
//    func percentEscaped() -> String {
//        return map { (key, value) in
//            let escapedKey = "\(key)".addingPercentEncoding(withAllowedCharacters: .urlQueryValueAllowed) ?? ""
//            let escapedValue = "\(value)".addingPercentEncoding(withAllowedCharacters: .urlQueryValueAllowed) ?? ""
//            return escapedKey + "=" + escapedValue
//            }
//            .joined(separator: "&")
//    }
//}
//
//extension CharacterSet {
//    static let urlQueryValueAllowed: CharacterSet = {
//        let generalDelimitersToEncode = ":#[]@" // does not include "?" or "/" due to RFC 3986 - Section 3.4
//        let subDelimitersToEncode = "!$&'()*+,;="
//
//        var allowed = CharacterSet.urlQueryAllowed
//        allowed.remove(charactersIn: "\(generalDelimitersToEncode)\(subDelimitersToEncode)")
//        return allowed
//    }()
//}
//
