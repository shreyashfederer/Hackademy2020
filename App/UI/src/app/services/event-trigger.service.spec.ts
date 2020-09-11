import { TestBed } from '@angular/core/testing';

import { EventTriggerService } from './event-trigger.service';

describe('EventTriggerService', () => {
  let service: EventTriggerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EventTriggerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
