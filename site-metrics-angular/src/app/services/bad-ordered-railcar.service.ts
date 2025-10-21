import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BadOrderedRailcar } from '../components/railcar-inspection/models/inspections';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BadOrderedRailcarService {

  private baseUrl = environment.apiUrl.find(url => url.includes('localhost')) || environment.apiUrl[0];

  constructor(private http: HttpClient) { }

// isActive bad orders
getActiveBadOrders(): Observable<BadOrderedRailcar[]> {
  const params = new HttpParams().set('ref', 'isActive');

  return this.http.get<BadOrderedRailcar[]>(`${this.baseUrl}/bad-orders`, { params });
}

  getAllBadOrders(): Observable<BadOrderedRailcar[]> {
    return this.http.get<BadOrderedRailcar[]>(`${this.baseUrl}/bad-orders`);
  }

  updateBadOrder(id: string, data: BadOrderedRailcar): Observable<BadOrderedRailcar> {
    return this.http.put<BadOrderedRailcar>(`${this.baseUrl}/bad-orders/${id}`, data);
  }
}
