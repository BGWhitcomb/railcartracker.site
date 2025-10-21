import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class TableService {
  private rowLoadingSubject = new BehaviorSubject<boolean>(false);
  rowLoading$ = this.rowLoadingSubject.asObservable();

  setRowLoading(value: boolean) {
    this.rowLoadingSubject.next(value);
  }
}