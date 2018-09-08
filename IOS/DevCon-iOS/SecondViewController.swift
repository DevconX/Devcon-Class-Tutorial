//
//  SecondViewController.swift
//  DevCon-iOS
//
//  Created by Hijazi on 15/9/17.
//  Copyright © 2017 iReka Soft. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {
  
  @IBOutlet weak var lbl_data: UILabel!
  
  var someStringInfo : String?
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    if let string = someStringInfo {
      
      lbl_data.text = string
      
    }
    
  }
  
  
  /*
   // MARK: - Navigation
   
   // In a storyboard-based application, you will often want to do a little preparation before navigation
   override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
   // Get the new view controller using segue.destinationViewController.
   // Pass the selected object to the new view controller.
   }
   */
  
}
