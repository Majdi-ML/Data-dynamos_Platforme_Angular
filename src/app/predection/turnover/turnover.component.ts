import { Component } from '@angular/core';
import * as XLSX from 'xlsx';

@Component({
  selector: 'app-turnover',
  templateUrl: './turnover.component.html',
  styleUrls: ['./turnover.component.css']
})
export class TurnoverComponent {
  data: any[][] = [];
  headers: string[] = [];
  filteredData: any[][] = [];
  searchTerm: string = '';

  constructor() {
    this.readExcelFile();
  }

  readExcelFile(): void {
    this.getFile('predicted2.xlsx').then((fileContent: ArrayBuffer) => {
      const workbook = XLSX.read(this.arrayBufferToBase64(fileContent), { type: 'base64' });
      const sheetName = workbook.SheetNames[0];
      const worksheet = workbook.Sheets[sheetName];

      this.data = XLSX.utils.sheet_to_json(worksheet, { header: 1 }) || [];
      this.headers = this.data.shift() || [];

      this.filterData(this.searchTerm); // Initial filtering with empty search term
    }).catch((error) => {
      console.error('Error reading file:', error);
    });
  }

  filterData(term: string): void {
    this.filteredData = this.data.filter(row => {
      // Modify the condition according to your filtering criteria
      return row[0].toLowerCase().includes(term.toLowerCase()) ||
             row[1].toLowerCase().includes(term.toLowerCase()) ||
             row[2].toLowerCase().includes(term.toLowerCase());
    });
  }

  getFile(filename: string): Promise<ArrayBuffer> {
    return new Promise<ArrayBuffer>((resolve, reject) => {
      const filePath = `assets/${filename}`;
      const xhr = new XMLHttpRequest();

      xhr.onload = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
          resolve(xhr.response);
        } else {
          reject(xhr.statusText);
        }
      };

      xhr.onerror = () => {
        reject(xhr.statusText);
      };

      xhr.open('GET', filePath);
      xhr.responseType = 'arraybuffer';
      xhr.send();
    });
  }

  private arrayBufferToBase64(buffer: ArrayBuffer): string {
    let binary = '';
    const bytes = new Uint8Array(buffer);
    const len = bytes.byteLength;
    for (let i = 0; i < len; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    return window.btoa(binary);
  }

  onSearchChange(event: any): void {
    this.searchTerm = event.target.value;
    this.filterData(this.searchTerm);
  }
}
