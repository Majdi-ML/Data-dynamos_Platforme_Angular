import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { ReactiveFormComponent } from './reactive-form/reactive-form.component';
import { EmployePageComponent } from './dashboard/employe-page/employe-page.component';
import { CeopageComponent } from './dashboard/ceopage/ceopage.component';
const routes: Routes = [
  {path:'home',component:HomeComponent},
  {path:'login',component:ReactiveFormComponent},
  {path:'employee',component: EmployePageComponent },
  {path:'ceopage',component:CeopageComponent },
  //route par défaut
  {path:'', redirectTo:'employee', pathMatch:'full'},
  //route not found
  {path:'**', component:NotFoundComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
