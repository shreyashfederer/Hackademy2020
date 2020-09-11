import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-budget',
  templateUrl: './budget.component.html',
  styleUrls: ['./budget.component.css']
})
export class BudgetComponent implements OnInit {

  currency = 1
  symbol
  fractionSize
  number = 1
  total: number
  emailAddress

  rooms = [
    { room: 'Living Room', budget: 4550 },
    { room: 'Master Bedroom', budget: 2795 },
    { room: 'Office', budget: 1300 },
    { room: 'Guest Room', budget: 100 },
    { room: 'Dining Room', budget: 700 },
    { room: 'Outdoors', budget: 1000 },
    { room: 'Laundry Room', budget: 1000 },
    { room: 'Misc', budget: 500 },
    { room: 'kitchen', budget: 3000 }
  ];

  constructor() { }

  ngOnInit(): void {
  }

  test() {
    var budget = this.total;
    for(var index in this.rooms){
       budget -= this.rooms[index].budget; 
    }
    return budget;
  }

  delete(index) {
    this.rooms.splice(index, 1);
  }

  add(addRoom: string, addBudget: number) {
    this.rooms.push({room: addRoom, budget: addBudget});
  }

  email(emailAddress: string) {
    var data = ""
    for(var index in this.rooms){
       data += this.rooms[index].room +': $'+this.rooms[index].budget + '.\r\n  '; 
    }
    
    window.open('mailto:'+ emailAddress +'?subject=Finance&body='+data);
  }

}
