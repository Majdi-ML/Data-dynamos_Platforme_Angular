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
import { TrainingNeedsComponent } from './predection/training-needs/training-needs.component';
import { ProfilingComponent } from './predection/profiling/profiling.component';
import { ButtonModule } from 'primeng/button';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { ProfilingService } from './profiling-service/profiling-service.service';
import { SatisfactionService } from './satisfaction-service/satisfaction-service.service';
import { CoursesService } from './courses-service/courses-srvice.service';
import { RecommendedCourse } from './courses-service/courses-srvice.service';
import { PopupComponent } from './popup/popup.component';
import { MatDialogModule } from '@angular/material/dialog';
import { SatisfactionComponent } from './predection/satisfaction/satisfaction.component';

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
    TrainingNeedsComponent, 
    ProfilingComponent,
    PopupComponent,
    SatisfactionComponent


    

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
    ButtonModule,
    HttpClientModule,
    MatDialogModule,
    // Autres configurations
  ],
  providers: [HttpClient, ProfilingService,SatisfactionService,CoursesService],
  bootstrap: [AppComponent]
})
export class AppModule { }
