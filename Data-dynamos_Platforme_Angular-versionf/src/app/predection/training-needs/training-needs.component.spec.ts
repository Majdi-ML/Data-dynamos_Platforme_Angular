import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingNeedsComponent } from './training-needs.component';

describe('TrainingNeedsComponent', () => {
  let component: TrainingNeedsComponent;
  let fixture: ComponentFixture<TrainingNeedsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TrainingNeedsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TrainingNeedsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
