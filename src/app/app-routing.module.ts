import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './component/login/login.component';
import { RegisterComponent } from './component/register/register.component';
import { ForgotPasswordComponent } from './component/forgot-password/forgot-password.component';
import { EmployePageComponent } from './dashboard/employe-page/employe-page.component';
import { CeopageComponent } from './dashboard/ceopage/ceopage.component';
import { SalaryComponent } from './dashboard/salary/salary.component';
import { LeaveComponent } from './dashboard/leave/leave.component';
import { AttendanceComponent } from './dashboard/attendance/attendance.component';
import { TrainingComponent } from './dashboard/training/training.component';
import { TurnoverComponent } from './predection/turnover/turnover.component';
import { SatisfactionComponent } from './predection/satisfaction/satisfaction.component';
import { TrainingNeedsComponent } from './predection/training-needs/training-needs.component';
import { ProfilingComponent } from './predection/profiling/profiling.component';
//import { NotFoundComponent } from './not-found/not-found.component';

const routes: Routes = [
  {path: '', redirectTo:'login', pathMatch:'full'},
  {path: 'login', component : LoginComponent},
 // {path: 'dashboard', component : DashboardComponent},
  {path: 'register', component : RegisterComponent},
 // {path: 'varify-email', component : VarifyEmailComponent},
  {path: 'forgot-password', component : ForgotPasswordComponent},
  {path:'employee',component: EmployePageComponent },
  {path:'ceopage',component:CeopageComponent },
  //{path : 'file-upload', component:FileuploadComponent}
  {path:'salary',component:SalaryComponent },
  {path:'leave',component:LeaveComponent },
  {path:'attendance',component:AttendanceComponent },
  {path:'training',component:TrainingComponent },
  {path:'turnover',component:TurnoverComponent },
  {path:'satisfaction',component:SatisfactionComponent },
  {path:'training-needs',component:TrainingNeedsComponent },
  {path:'profiling',component:ProfilingComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
