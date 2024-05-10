import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/compat/auth';
import { GoogleAuthProvider } from '@angular/fire/auth';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  currentUserEmail: string = '';

  constructor(private fireauth: AngularFireAuth, private router: Router) { }

  login(email: string, password: string) {
    this.fireauth.signInWithEmailAndPassword(email, password).then(res => {
      localStorage.setItem('token', 'true');

      if (res.user?.emailVerified == true) {
        this.currentUserEmail = email; // Store the current user's email
        this.redirectUser(email);
      } else {
        this.router.navigate(['/verify-email']);
      }

    }, err => {
      alert(err.message);
      this.router.navigate(['/login']);
    });
  }

  private redirectUser(email: string) {
    // Check user's email and redirect accordingly
    if (email === 'landolsi.aziz9@gmail.com') {
      this.router.navigate(['/ceopage']);
    } else if (email === 'majdi.melliti@esprit.tn') {
      this.router.navigate(['/employee']);
    } else {
      this.router.navigate(['/dashboard']);
    }
  }
  
  // register method
  register(email: string, password: string) {
    this.fireauth.createUserWithEmailAndPassword(email, password).then(res => {
      alert('Registration Successful');
      this.sendEmailForVarification(res.user);
      this.router.navigate(['/login']);
    }, err => {
      alert(err.message);
      this.router.navigate(['/register']);
    });
  }

  // sign out
  logout() {
    this.fireauth.signOut().then(() => {
      localStorage.removeItem('token');
      this.router.navigate(['/login']);
    }, err => {
      alert(err.message);
    });
  }

  // forgot password
  forgotPassword(email: string) {
    this.fireauth.sendPasswordResetEmail(email).then(() => {
      this.router.navigate(['/verify-email']);
    }, err => {
      alert('Something went wrong');
    });
  }

  // email varification
  sendEmailForVarification(user: any) {
    user.sendEmailVerification().then(() => {
      this.router.navigate(['/varify-email']);
    }, (err: any) => {
      alert('Something went wrong. Not able to send mail to your email.');
    });
  }

  // sign in with google
  googleSignIn() {
    return this.fireauth.signInWithPopup(new GoogleAuthProvider).then(res => {
      this.router.navigate(['/employee']);
      localStorage.setItem('token', JSON.stringify(res.user?.uid));
    }, err => {
      alert(err.message);
    });
  }


  getCurrentUser() {
    return new Promise<any>((resolve, reject) => {
      this.fireauth.onAuthStateChanged(user => {
        if (user) {
          resolve(user);
        } else {
          reject('No user logged in');
        }
      });
    });
  }
}
