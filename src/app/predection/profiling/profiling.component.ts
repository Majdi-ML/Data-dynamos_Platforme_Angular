import { Component, NgModule } from '@angular/core';
import { NavbarComponent } from 'src/app/navbar/navbar.component';
import { SidenavbarComponent } from 'src/app/sidenavbar/sidenavbar.component';

@Component({
  selector: 'app-profiling',
  templateUrl: './profiling.component.html',
  styleUrls: ['./profiling.component.css']
})
export class ProfilingComponent {
  softwareCandidates: any[] = [];
  telecomCandidates: any[] = [];

  onCandidatesLoaded(event: { softwareCandidates: any[], telecomCandidates: any[] }) {
    this.softwareCandidates = event.softwareCandidates;
    this.telecomCandidates = event.telecomCandidates;
  }
}


  // autres propriétés du module...

export class ProfilingModule { }
