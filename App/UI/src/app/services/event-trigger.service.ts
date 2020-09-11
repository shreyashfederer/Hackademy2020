import { Injectable, Output, EventEmitter } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EventTriggerService {

  @Output() selectedButton: EventEmitter<Object> = new EventEmitter();

  constructor() { }

  setFeature(feature: string) {
    this.selectedButton.emit({
      "button": feature
    })
  }
}
