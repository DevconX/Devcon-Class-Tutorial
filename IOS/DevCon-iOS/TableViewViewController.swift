//
//  TableViewViewController.swift
//  DevCon-iOS
//
//  Created by Hijazi on 15/9/17.
//  Copyright © 2017 iReka Soft. All rights reserved.
//

import UIKit

class TableViewViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
  
  
  var myArray = ["box 1", "box 2", "box 3"]
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    title = "UITableView"
    
  }
  
  // 
  
  func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    
    return myArray.count
    
    

  }
  
  @IBAction func segmentedControlChanged(_ sender: UISegmentedControl) {
    
    print("selected idx \(sender.selectedSegmentIndex)")
    
    
  }
  
  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    
    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell")!
    
    cell.textLabel?.text = myArray[indexPath.row]
    
    return cell
    
  }
  
  func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    
    print("you have selected \(indexPath.row)")
    tableView.deselectRow(at: indexPath, animated: true)
    
    performSegue(withIdentifier: "showDetail", sender: indexPath)
    
  }
  
  override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    
    if (segue.identifier == "showDetail"){
      
      print("prepare for segue \(#function)")
      
      let indexPath = sender as! IndexPath
      
      let string = myArray[indexPath.row]
      
      if let vc = segue.destination as? SecondViewController {
        
        
        vc.someStringInfo = string
        
        
      }
      
    }
    
  }
  
}
