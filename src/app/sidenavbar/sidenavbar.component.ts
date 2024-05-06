import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/shared/auth.service';

@Component({
  selector: 'app-sidenavbar',
  templateUrl: './sidenavbar.component.html',
  styleUrls: ['./sidenavbar.component.css']
})
export class SidenavbarComponent implements OnInit {
  isCEO: boolean = false;
  isManager: boolean = false;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    // Récupérer les informations sur l'utilisateur connecté
    this.authService.getCurrentUser().then(user => {
      // Vérifier le type d'utilisateur et définir les propriétés correspondantes
      if (user.email === 'landolsi.aziz9@gmail.com') {
        this.isCEO = true;
      } else if (user.email === 'majdi.melliti@esprit.tn') {
        this.isManager = true;
      }
    }).catch(err => {
      console.error('Error getting current user:', err);
    });
  }
}
