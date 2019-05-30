//
//  Node.swift
//  CarInterface
//
//  Created by Kardo Dastin on 2019-05-14.
//  Copyright © 2019 TeamLate. All rights reserved.
//

import Foundation
import UIKit
@objcMembers class node {
    
    dynamic var id: String = ""
   dynamic var source: CGPoint
   dynamic var destination: CGPoint
    
    convenience init(
        id: String,
        source: CGPoint,
        destination: CGPoint
        ){
        self.id = id
        self.source = source
        self.destination = destination
        
    }
    
}
