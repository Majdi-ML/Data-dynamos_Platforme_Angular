import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CeopageComponent } from './ceopage.component';

describe('CeopageComponent', () => {
  let component: CeopageComponent;
  let fixture: ComponentFixture<CeopageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CeopageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CeopageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
