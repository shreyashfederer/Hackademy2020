import { Component, OnInit } from '@angular/core';
import { HomeService } from 'src/app/services/home.service';

@Component({
  selector: 'app-upload-bills',
  templateUrl: './upload-bills.component.html',
  styleUrls: ['./upload-bills.component.css']
})
export class UploadBillsComponent implements OnInit {

  fileToUpload: File = null;
  showTable: boolean;
  billData = [];

  constructor(private HomeService: HomeService) { }

  ngOnInit(): void {
    this.showTable = true;
  }

  OnSubmit() {
    this.HomeService.uploadFile(this.fileToUpload).subscribe((data) => {
      console.log(data);
      let i=1;
      for (let k in data) {
        let obj = {
          "sno": i,
          "category": k,
          "amount": data[k]
        }
        this.billData.push(obj);
        ++i;
      }
      this.showTable = false;
    })
  }

  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);  
  }

}
