import { Component, OnInit } from '@angular/core';
import { EventTriggerService } from 'src/app/services/event-trigger.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  isHome: boolean;
  isOffer: boolean;
  isNotifications: boolean;
  isBudget: boolean;
  isExpense: boolean;
  isBills: boolean;
  

  constructor(private EventService: EventTriggerService) { }

  ngOnInit(): void {

    this.isBills = this.isOffer = this.isBudget = this.isNotifications = this.isExpense = true;
    this.isHome = false;

    this.EventService.selectedButton.subscribe((data) => {
      console.log(data['button'])
      if(data['button'] == 'HOME') {
        this.isHome = false;
        this.isBills = this.isBudget = this.isExpense = this.isNotifications = this.isOffer = true;
      } else if(data['button'] == 'OFFER') {
        this.isOffer = false;
        this.isBills = this.isBudget = this.isExpense = this.isNotifications = this.isHome = true;
      } else if(data['button'] == 'NOTIFICATION') {
        this.isNotifications = false;
        this.isBills = this.isBudget = this.isExpense = this.isHome = this.isOffer = true;
      } else if(data['button'] == 'BUDGET') {
        this.isBudget = false;
        this.isBills = this.isHome = this.isExpense = this.isNotifications = this.isOffer = true;
      } else if(data['button'] == 'EXPENSE') {
        this.isExpense = false;
        this.isBills = this.isBudget = this.isHome = this.isNotifications = this.isOffer = true;
      } else if(data['button'] == 'BILL') {
        this.isBills = false;
        this.isHome = this.isBudget = this.isExpense = this.isNotifications = this.isOffer = true;
      }
    })
  }

}
