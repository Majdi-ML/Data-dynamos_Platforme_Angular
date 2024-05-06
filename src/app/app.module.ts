import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarModule } from 'primeng/sidebar';
import {AngularFireModule} from '@angular/fire/compat'
import { environment } from 'src/environments/environment';
import { LoginComponent } from './component/login/login.component';
import { RegisterComponent } from './component/register/register.component';
import { FormsModule } from '@angular/forms';
import { ForgotPasswordComponent } from './component/forgot-password/forgot-password.component';
import { NavbarComponent } from './navbar/navbar.component';
import { SidenavbarComponent } from './sidenavbar/sidenavbar.component';
import { Sidenavbar2Component } from './sidenavbar2/sidenavbar2.component';
import { CeopageComponent } from './dashboard/ceopage/ceopage.component';
import { EmployePageComponent } from './dashboard/employe-page/employe-page.component';
import { FooterComponent } from './footer/footer.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { SalaryComponent } from './dashboard/salary/salary.component';
import { LeaveComponent } from './dashboard/leave/leave.component';
import { AttendanceComponent } from './dashboard/attendance/attendance.component';
import { TrainingComponent } from './dashboard/training/training.component';
import { TurnoverComponent } from './predection/turnover/turnover.component';
import { SatisfactionComponent } from './predection/satisfaction/satisfaction.component';
import { TrainingNeedsComponent } from './predection/training-needs/training-needs.component';
import { ProfilingComponent } from './predection/profiling/profiling.component';
import { ButtonModule } from 'primeng/button';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    ForgotPasswordComponent,
    NavbarComponent,
    SidenavbarComponent,
    CeopageComponent,
    EmployePageComponent,
    FooterComponent,
    SalaryComponent,
    LeaveComponent,
    AttendanceComponent, 
    TrainingComponent,
    TurnoverComponent,
    SatisfactionComponent,
    TrainingNeedsComponent, 
    ProfilingComponent,
    Sidenavbar2Component,
    

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AngularFireModule.initializeApp(environment.firebase),
    FormsModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatListModule,
    MatToolbarModule,
    MatIconModule,
    SidebarModule,
    ButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
