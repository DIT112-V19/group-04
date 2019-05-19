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
    
    dynamic var id: String = ""
    var location: CGPoint!
   
    
    convenience init(
        id: String,
        location: CGPoint
        ){
        self.init(id: id, location: location)
        self.id = id
        self.location = location
    }
}
