import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Sidenavbar2Component } from './sidenavbar2.component';

describe('Sidenavbar2Component', () => {
  let component: Sidenavbar2Component;
  let fixture: ComponentFixture<Sidenavbar2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Sidenavbar2Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Sidenavbar2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
