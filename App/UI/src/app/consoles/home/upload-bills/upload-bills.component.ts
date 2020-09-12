import { Component, OnInit } from '@angular/core';
import { HomeService } from 'src/app/services/home.service';

@Component({
  selector: 'app-upload-bills',
  templateUrl: './upload-bills.component.html',
  styleUrls: ['./upload-bills.component.css']
})
export class UploadBillsComponent implements OnInit {

  chooseFile;

  constructor(private HomeService: HomeService) { }

  ngOnInit(): void {
  }

  OnSubmit() {
    this.HomeService.uploadFile(this.chooseFile).subscribe((data) => {
      console.log(data);
    })
  }

}
