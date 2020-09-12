import { Injectable } from '@angular/core';
import { WebService } from './web-service.service';
import { HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class HomeService {

  constructor(private WebService: WebService) { }

  addBudget(user: string,  spent: any, total: number) {
    return this.WebService.post('budget', {
      "user": user,
      "spent": spent,
      "total": total
    })
  }

  uploadFile(files) {
    const formData: FormData = new FormData();
    formData.append('fileKey', files, files.name);
    return this.WebService.post('ocr', formData)
  }

  addExpenses(user: string, spent: any) {
    return this.WebService.post('expenses', {
      "user": user,
      "spent": spent
    })
  }
}
