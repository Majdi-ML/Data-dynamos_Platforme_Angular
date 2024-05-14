import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProfilingService {
  constructor(private http: HttpClient) { }

  executeModel(): Observable<any> {
    return this.http.post<any>('http://localhost:5000/profiling', {});
  }
}
