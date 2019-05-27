//
//  File.swift
//  CarInterface
//
//  Created by Kardo Dastin on 2019-05-14.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import Foundation
import UIKit

@objcMembers class User{
    
    dynamic var id: String = ""
    var source: CGPoint!
    var destination: CGPoint!
    
    
    convenience init(
        id: String,
        source: CGPoint,
        destination: CGPoint
        ){
        self.init(id: id, source: source, destination: destination)
        self.id = id
        self.source = source
        self.destination = destination
        
    }
    
}
