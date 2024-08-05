import {ComponentFixture, TestBed} from '@angular/core/testing';
import {Ros2CommunicatorComponent} from "./ros2-communicator.component";
import {TranslateLoader, TranslateModule} from "@ngx-translate/core";
import {Observable, of} from "rxjs";

describe('Ros2CommunicatorComponent', () => {
  let fixture: ComponentFixture<Ros2CommunicatorComponent>;
  let component: Ros2CommunicatorComponent;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Ros2CommunicatorComponent],
      imports: [TranslateModule.forRoot({
        loader: {
          provide: TranslateLoader, useValue: {
            getTranslation(): Observable<Record<string, string>> {
              return of({});
            }
          }
        }
      })],
    }).compileComponents();

    fixture = TestBed.createComponent(Ros2CommunicatorComponent);
    component = fixture.componentInstance;
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });
});
