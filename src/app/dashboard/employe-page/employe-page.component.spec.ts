import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EmployePageComponent } from './employe-page.component';

describe('EmployePageComponent', () => {
  let component: EmployePageComponent;
  let fixture: ComponentFixture<EmployePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EmployePageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EmployePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
