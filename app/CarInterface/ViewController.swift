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

class ViewController: UIViewController {

    @IBOutlet weak var GetButton: UIButton!
    @IBOutlet weak var goButton: UIButton!
    let url = "https://prebeo.serveo.net/api/getlocation"
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

    @IBAction func getButtonPressed(_ sender: Any) {
        self.getCarLocation()
    }
    
    
    @IBAction func goButtonPressed(_ sender: Any) {
        self.convert()
        self.postReview()
    }
    
    
    func postReview() {
        
        guard let url = URL(string: self.url) else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("id=\(userId)", forHTTPHeaderField: "Cookie")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        let jsonEncoder = JSONEncoder()
        let payLoad = PayLoad(location: source, destination: destination)
        let httpBody = try? jsonEncoder.encode(payLoad)
        print(String(decoding: httpBody!, as: UTF8.self))
        request.httpBody = httpBody
        URLSession.shared.dataTask(with: request) { (recData, response, error) in
            if let data = recData {
                do{
                    let json = try JSONSerialization.jsonObject(with: data, options: [])
                    print("JSON IS ",json)
                  } catch {
                    print("failed ",error.localizedDescription)
                }
            }
            }.resume()
    }
    
    
    
    
    func getCarLocation(){
        
        let car = carManager.shared.theCar
        guard let url = URL(string: self.url) else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.setValue("id=\(userId)", forHTTPHeaderField: "Cookie")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        URLSession.shared.dataTask(with: request) { (recData, response, error) in
            if let data = recData {
                do{
                    let response = try? newJSONDecoder().decode(Response.self, from: data)
                    var point = CGPoint()
                    point.x = CGFloat(response!.carLocation[0])
                    point.y = CGFloat(response!.carLocation[1])
                    debugPrint(point)
                    car.location = point
                  }
                  }
            }.resume()
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
struct PayLoad: Codable {
    let location, destination: [Int]
}
struct Response: Codable {
    let carLocation: [Int]
}

func newJSONDecoder() -> JSONDecoder {
    let decoder = JSONDecoder()
    return decoder
}

func newJSONEncoder() -> JSONEncoder {
    let encoder = JSONEncoder()
    return encoder
}

extension URLSession {
    fileprivate func codableTask<T: Codable>(with url: URL, completionHandler: @escaping (T?, URLResponse?, Error?) -> Void) -> URLSessionDataTask {
        return self.dataTask(with: url) { data, response, error in
            guard let data = data, error == nil else {
                completionHandler(nil, response, error)
                return
            }
            completionHandler(try? newJSONDecoder().decode(T.self, from: data), response, nil)
        }
    }
    
    func payLoadTask(with url: URL, completionHandler: @escaping (PayLoad?, URLResponse?, Error?) -> Void) -> URLSessionDataTask {
        return self.codableTask(with: url, completionHandler: completionHandler)
    }
}
