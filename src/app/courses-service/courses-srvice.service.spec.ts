import { TestBed } from '@angular/core/testing';

import { CoursesSrviceService } from './courses-srvice.service';

describe('CoursesSrviceService', () => {
  let service: CoursesSrviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CoursesSrviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
