import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SatisfactionComponent } from './satisfaction.component';

describe('SatisfactionComponent', () => {
  let component: SatisfactionComponent;
  let fixture: ComponentFixture<SatisfactionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SatisfactionComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SatisfactionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
