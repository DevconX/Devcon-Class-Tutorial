//
//  InterfaceBuilderViewController.swift
//  DevCon-iOS
//
//  Created by Hijazi on 15/9/17.
//  Copyright © 2017 iReka Soft. All rights reserved.
//

import UIKit

class InterfaceBuilderViewController: UIViewController {
  
  
  
  @IBOutlet weak var label: UILabel!
  @IBOutlet weak var textField: UITextField!

  override func viewDidLoad() {
    super.viewDidLoad()
    
  }
  
  override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()

  }
  
  @IBAction func doSomething(_ sender: UIButton) {
    
    label.text = textField.text
    
  }
  
  
}
