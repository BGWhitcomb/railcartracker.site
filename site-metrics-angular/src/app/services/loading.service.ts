import { Injectable } from '@angular/core';
import { BehaviorSubject, debounceTime, distinctUntilChanged, Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class LoadingService {
  private loadingSubject = new BehaviorSubject<boolean>(false);
  private activeRequests = 0;


  loading$: Observable<boolean> = this.loadingSubject
    .asObservable()
    .pipe(
      debounceTime(75),
      distinctUntilChanged()
    );

  show() {
    this.activeRequests++;
    this.loadingSubject.next(true);
  }

  hide() {
    this.activeRequests = Math.max(0, this.activeRequests - 1);
    if (this.activeRequests === 0) {
      this.loadingSubject.next(false);
    }
  }
}
