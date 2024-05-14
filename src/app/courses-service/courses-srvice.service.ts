import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

export interface RecommendedCourse {
  empIndex: number;
  RecommendedCourse: string;
  SimilarityScore: number;
  CourseRating: number;
  department: string;
}

@Injectable({
  providedIn: 'root'
})
export class CoursesService {
  private apiUrl: string = 'http://localhost:5000/recommendations';

  constructor(private http: HttpClient) { }

  getRecommendedCourses(empName: string, department: string): Observable<RecommendedCourse[]> {
    const data = { emp_name: empName, department: department };
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };
    return this.http.post<RecommendedCourse[]>(this.apiUrl, data, httpOptions).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: HttpErrorResponse) {
    console.error(error);
    return throwError(error.message);
  }
}
