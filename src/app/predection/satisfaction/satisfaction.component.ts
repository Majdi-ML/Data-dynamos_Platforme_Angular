import { Component } from '@angular/core';
import { SatisfactionService,EmployeeSatisfactionPrediction } from 'src/app/satisfaction-service/satisfaction-service.service';

@Component({
  selector: 'app-satisfaction',
  templateUrl: './satisfaction.component.html',
  styleUrls: ['./satisfaction.component.css']
})
export class SatisfactionComponent {
  predictions: EmployeeSatisfactionPrediction[] = [];
  empName: string = '';
  department: string = '';
  errorMessage: string = '';

  constructor(private satisfactionService: SatisfactionService) { }

  fetchPredictions() {
    this.satisfactionService.getSatisfaction(this.empName, this.department).subscribe(
      (data: EmployeeSatisfactionPrediction[]) => {
        this.predictions = data;
        console.log(data)
      },
      (error: Error) => {
        console.error('Error:', error);
        this.errorMessage = 'Failed to fetch predictions from the server.';
      }
    );
  }
}
