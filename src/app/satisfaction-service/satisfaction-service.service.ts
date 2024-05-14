import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

export interface EmployeeSatisfactionPrediction {
  NAME_EMP: string;
  TYPE_DIPLOMA: string;
  EXP_YEARS: number;
  GENDER: string;
  POSITION: string;
  predicted_satisfaction: number;
}

@Injectable({
  providedIn: 'root'
})
export class SatisfactionService {
  private apiUrl: string = 'http://localhost:5000/satisfaction';

  constructor(private http: HttpClient) { }

  getSatisfaction(empName: string, department: string): Observable<EmployeeSatisfactionPrediction[]> {
    const data = { emp_name: empName, department: department };
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };
    return this.http.post<EmployeeSatisfactionPrediction[]>(this.apiUrl, data, httpOptions).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: HttpErrorResponse) {
    console.error('An error occurred:', error.error);
    return throwError('Something bad happened; please try again later.');
  }
}
