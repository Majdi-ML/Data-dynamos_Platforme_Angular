import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.css']
})
export class PopupComponent implements OnInit {
  firstName: string; // Définissez le type de firstName comme string
  constructor(@Inject(MAT_DIALOG_DATA) public data: { name: string }) { // Définissez le type de data comme { name: string }
    this.firstName = data.name;
  }

  ngOnInit(): void {
  }

}
