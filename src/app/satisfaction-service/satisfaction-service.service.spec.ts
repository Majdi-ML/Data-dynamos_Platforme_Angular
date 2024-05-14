import { TestBed } from '@angular/core/testing';

import { SatisfactionService } from './satisfaction-service.service';

describe('SatisfactionServiceService', () => {
  let service: SatisfactionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SatisfactionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
