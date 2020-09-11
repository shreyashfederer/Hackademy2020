import { TestBed } from '@angular/core/testing';

import { WebService } from './web-service.service';

describe('WebServiceService', () => {
  let service: WebService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(WebService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
