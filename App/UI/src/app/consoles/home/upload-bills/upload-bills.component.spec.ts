import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadBillsComponent } from './upload-bills.component';

describe('UploadBillsComponent', () => {
  let component: UploadBillsComponent;
  let fixture: ComponentFixture<UploadBillsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UploadBillsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UploadBillsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
