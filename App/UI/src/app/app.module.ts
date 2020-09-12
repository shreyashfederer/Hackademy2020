import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { WelcomeComponent } from './welcome/welcome.component';
import { LoginComponent } from './consoles/login/login.component';
import { HomeComponent } from './consoles/home/home.component';
import { NavBarComponent } from './consoles/home/nav-bar/nav-bar.component';
import { ExpensesComponent } from './consoles/home/expenses/expenses.component';
import { HomeDisplayComponent } from './consoles/home/home-display/home-display.component';
import { OffersComponent } from './consoles/home/offers/offers.component';
import { NotificationsComponent } from './consoles/home/notifications/notifications.component';
import { BudgetComponent } from './consoles/home/budget/budget.component';
import { UploadBillsComponent } from './consoles/home/upload-bills/upload-bills.component';
import { VisualComponent } from './consoles/home/visual/visual.component';

@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    LoginComponent,
    HomeComponent,
    NavBarComponent,
    ExpensesComponent,
    HomeDisplayComponent,
    OffersComponent,
    NotificationsComponent,
    BudgetComponent,
    UploadBillsComponent,
    VisualComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
