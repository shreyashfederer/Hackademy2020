import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class WebService {

  readonly ROOT_URL;

  constructor(private http: HttpClient) { 
    this.ROOT_URL = "http://35.230.145.24:8000";
  }

  get(url: string) {
    return this.http.get(`${this.ROOT_URL}/${url}`);
  }

  post(url: string, payload: Object) {
    return this.http.get(`${this.ROOT_URL}/${url}`, payload);
  }

  /*postFile(url: string, payload: Object) {
    return this.http.get(`${this.ROOT_URL}/${url}`, payload, );
  }*/
  
  patch(url: string, payload: Object) {
    return this.http.patch(`${this.ROOT_URL}/${url}`, payload)
  }

  delete(url: string) {
    return this.http.delete(`${this.ROOT_URL}/${url}`)
  }

}
