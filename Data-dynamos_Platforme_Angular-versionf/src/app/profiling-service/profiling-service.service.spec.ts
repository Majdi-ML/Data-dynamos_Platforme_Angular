import { TestBed } from '@angular/core/testing';

import { ProfilingServiceService } from './profiling-service.service';

describe('ProfilingServiceService', () => {
  let service: ProfilingServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProfilingServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
