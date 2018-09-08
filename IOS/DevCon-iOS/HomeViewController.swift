//
//  HomeViewController.swift
//  DevCon-iOS
//
//  Created by Hijazi on 15/9/17.
//  Copyright © 2017 iReka Soft. All rights reserved.
//

import UIKit

class HomeViewController: UIViewController {
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    title = "{title = \"title\"}"
    
  }
  
  override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()
    // Dispose of any resources that can be recreated.
  }
  
  override func prepare(for segue: UIStoryboardSegue, sender: Any?) {

    if (segue.identifier == "pushVC"){

      if let vc = segue.destination as? SecondViewController {
        
        vc.someStringInfo = "Secret String"
        
        
      }
    }
  }
  
}
