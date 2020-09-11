import { Component, OnInit } from '@angular/core';
import { EventTriggerService } from 'src/app/services/event-trigger.service';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {

  constructor(private EventService: EventTriggerService) { }

  ngOnInit(): void {
  }

  OnHome() {
    console.log("HOme Enters")
    this.EventService.setFeature("HOME");
  }

  OnOffers() {
    console.log("Offers Enters")
    this.EventService.setFeature("OFFER");
  }

  OnBudget() {
    console.log("Budgets Enters")
    this.EventService.setFeature("BUDGET");
  }

  OnNotifications() {
    console.log("Notifications Enters")
    this.EventService.setFeature("NOTIFICATION");
  }

  OnExpenses() {
    console.log("Expenses Enters")
    this.EventService.setFeature("EXPENSE");
  }

  OnBills() {
    console.log("Bills Enters")
    this.EventService.setFeature("BILL");
  }
}
