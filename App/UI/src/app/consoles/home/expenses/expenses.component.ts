import { Component, OnInit } from '@angular/core';
import { HomeService } from 'src/app/services/home.service';

@Component({
  selector: 'app-expenses',
  templateUrl: './expenses.component.html',
  styleUrls: ['./expenses.component.css']
})
export class ExpensesComponent implements OnInit {

  public rooms = [
        { room: 'Electronics', budget:80000 },
        { room: 'Grocery', budget: 900 },
        { room: 'Apparels', budget: 1300 },
        { room: 'Food', budget: 60 },
        { room: 'Furniture', budget: 12900 }
      /*  { room: 'Outdoors', budget: 0 },
        { room: 'Laundry Room', budget: 1000 },
        { room: 'Misc', budget: 500 },
        { room: 'kitchen', budget: 3000 } */
      ];

  constructor(private HomeService: HomeService) { }

  ngOnInit(): void {
  }


  delete(index) {
    this.rooms.splice(index, 1);
  }

  add(addRoom: string, addBudget: number) {
    this.rooms.push({room: addRoom, budget: addBudget});
  }

  save() {
    this.HomeService.addExpenses("Pawan", this.rooms).subscribe((data) => {
      console.log(data)
    })
  }

}
