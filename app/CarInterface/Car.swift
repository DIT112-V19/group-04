//
//  Car.swift
//  CarInterface
//
//  Created by Kardo Dastin on 2019-05-18.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import Foundation
import Foundation
import UIKit

@objcMembers class Car{
    
    dynamic var id: String = UUID.init().uuidString
    var location: CGPoint!
    
    
    convenience init(location: CGPoint){
        self.init(location: location)
        self.location = location
    }
}
