import { Component } from '@angular/core';
import { CoursesService, RecommendedCourse } from 'src/app/courses-service/courses-srvice.service';

@Component({
  selector: 'app-training-needs',
  templateUrl: './training-needs.component.html',
  styleUrls: ['./training-needs.component.css']
})
export class TrainingNeedsComponent {
  recommendedCourses: RecommendedCourse[] = [];
  empName: string = '';
  department: string = '';

  constructor(private coursesService: CoursesService) { }

  searchRecommendations(): void {
    this.coursesService.getRecommendedCourses(this.empName, this.department)
      .subscribe(
        (courses: RecommendedCourse[]) => {
          this.recommendedCourses = courses;
          console.log(courses)
        },
        (error: Error) => {
          console.error('Erreur lors de la récupération des recommandations de cours : ', error);
        }
      );
  }
}
