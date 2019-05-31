//
//  httpManager.swift
//  CarInterface
//
//  Created by Jean paul Massoud on 2019-05-29.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import Foundation
import UIKit

class httpManager {
    
    static let shared = httpManager()
    init() {}
    private let url = "https://loci.serveo.net/"
    private let getCall = "api/getlocation"
    private let postCall = "api/pickup"
    private var car = carManager.shared
    private var user = UserManager.shared
    private let cache = ImageCache.shared
    private let tools = Tools.shared
    
    
    
    
    
    @objc func updateCarLocation() {
        
        var target = CGPoint()
        guard let url = URL(string: String("\(self.url)\(self.getCall)")) else { return }
        var request = URLRequest(url: url)
        let jsonDecoder = JSONDecoder()
        request.httpMethod = "GET"
        request.setValue("id=\(self.user.theUser.id)", forHTTPHeaderField: "Cookie")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        URLSession.shared.dataTask(with: request) { (recData, response, error) in
            if let data = recData {
                do{
                    if let response = try? jsonDecoder.decode(Response.self, from: data){
                        var point = CGPoint()
                        point.x = CGFloat(response.carLocation[0])
                        point.y = CGFloat(response.carLocation[1])
                        debugPrint("respons cg point >>",point)
                        target = Tools.shared.deConverter(location: point)
                        self.car.theCar.location = target
                        debugPrint("respons converted >>",target)
                    }
                }
            }
            }.resume()
        return
    }
    
    
    
    func postContent() {
        
        var target = CGPoint()
        guard let url = URL (string: String("\(self.url)\(self.postCall)")) else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("id=\(user.theUser.id)", forHTTPHeaderField: "Cookie")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        let jsonEncoder = JSONEncoder()
        let jsonDecoder = JSONDecoder()
        let p1 = tools.converter(location: user.theUser.source)
        let p2 = tools.converter(location: user.theUser.destination)
        print("p1 >>\(p1)")
        print("p2 >>\(p2)")
        let payLoad = PayLoad(location: tools.toArray(point: p1), destination: tools.toArray(point: p2))
        print("payload >>",payLoad)
        let httpBody = try? jsonEncoder.encode(payLoad)
        print("http buddy",String(decoding: httpBody!, as: UTF8.self))
        request.httpBody = httpBody
        URLSession.shared.dataTask(with: request) { (recData, response, error) in
            if let data = recData {
                do{
                    if let response = try? jsonDecoder.decode(Response.self, from: data){
                        var point = CGPoint()
                        point.x = CGFloat(response.carLocation[0])
                        point.y = CGFloat(response.carLocation[1])
                        debugPrint("first respond >>\(point)")
                        target = Tools.shared.deConverter(location: point)
                        self.car.theCar.location = target
                    }
                }
            }
            }.resume()
        return
    }
    
    
    
}

struct PayLoad: Codable {
    let location, destination: [Int]
}
struct Response: Codable {
    let carLocation: [Int]
}




