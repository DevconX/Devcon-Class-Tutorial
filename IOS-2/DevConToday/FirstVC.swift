//
//  FirstVC.swift
//  DevConToday
//
//  Created by Hijazi on 20/8/17.
//  Copyright © 2017 iReka Soft / DevCon. All rights reserved.
//

import UIKit
import Alamofire

class FirstVC: UIViewController {
  
  @IBOutlet weak var lbl_main: UILabel!
  
  @IBOutlet weak var tf_main: UITextField!
  
  
  @IBAction func save(_ sender: Any) {
    
    UserDefaults.standard.set(tf_main.text, forKey: "NAME")
    
    UserDefaults.standard.synchronize()
    
    lbl_main.text = tf_main.text
    
    
  }
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    // Do any additional setup after loading the view.
    
    let name = UserDefaults.standard.string(forKey: "NAME")
    
    lbl_main.text = name
    
    Alamofire.request("https://httpbin.org/get").response { response in
      print("Request: \(response.request)")
      print("Response: \(response.response)")
      print("Error: \(response.error)")
      
      if let data = response.data, let utf8Text = String(data: data, encoding: .utf8) {
        print("Data: \(utf8Text)")
      }
    }
    
  }
  
  override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()
    // Dispose of any resources that can be recreated.
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
