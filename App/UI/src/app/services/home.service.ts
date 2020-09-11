import { Injectable } from '@angular/core';
import { WebService } from './web-service.service';

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
}
