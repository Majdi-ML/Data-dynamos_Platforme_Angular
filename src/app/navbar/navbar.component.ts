import { Component, Output, EventEmitter } from '@angular/core';
import { AuthService } from 'src/app/shared/auth.service';
import { ProfilingService } from '../profiling-service/profiling-service.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  userEmail: string = '';
  softwareCandidates: any[] = [];
  telecomCandidates: any[] = [];
  
  @Output() candidatesLoaded: EventEmitter<{ softwareCandidates: any[], telecomCandidates: any[] }> = new EventEmitter();

  constructor(private authService: AuthService, private profilingService: ProfilingService) { }

  ngOnInit(): void {
    this.getCurrentUserEmail();
  }

  getCurrentUserEmail() {
    this.userEmail = this.authService.currentUserEmail;
  }

  logout() {
    this.authService.logout();
  }

  executeModel() {
    this.profilingService.executeModel().subscribe(data => {
      this.softwareCandidates = data.software_candidates;
      this.telecomCandidates = data.telecom_candidates;
      this.candidatesLoaded.emit({ softwareCandidates: this.softwareCandidates, telecomCandidates: this.telecomCandidates });
    });
  }
}
