import { Component } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog'; // Importez MatDialog et MatDialogRef depuis @angular/material/dialog
import { PopupComponent } from 'src/app/popup/popup.component';
import { AuthService } from 'src/app/shared/auth.service';
@Component({
  selector: 'app-employe-page',
  templateUrl: './employe-page.component.html',
  styleUrls: ['./employe-page.component.css']
})
export class EmployePageComponent {

  userEmail: string = '';

  constructor(private dialog: MatDialog,private authService: AuthService) {} // Utilisez simplement MatDialog sans Inject
  ngOnInit(): void {
    this.getCurrentUserEmail();
  }

  getCurrentUserEmail() {
    this.userEmail = this.authService.currentUserEmail;
  }
  openDialog() {
    this.dialog.open(PopupComponent, {
      data: {
        name: this.userEmail
      }
});
  }
  
}
