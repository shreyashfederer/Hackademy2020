import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private Route: Router) { }

  ngOnInit(): void {
    console.log('ASY')
  }

  SignIn(a, b) {
    console.log('SignIn')
    this.Route.navigate(['/home'], a)
  }

  SignUp(a,b,c) {
    console.log(a)
    console.log(b)
    console.log(c)
  }

}
