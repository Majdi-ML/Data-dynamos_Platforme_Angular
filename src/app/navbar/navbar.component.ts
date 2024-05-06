import { Component } from '@angular/core';
import { AuthService } from 'src/app/shared/auth.service';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  userEmail: string='';

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.getCurrentUserEmail();
  }

  getCurrentUserEmail() {
    this.userEmail = this.authService.currentUserEmail; // Access the stored email
  }

  logout() {
    this.authService.logout();
  }
}
