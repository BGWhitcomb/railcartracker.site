import { Component, Input } from '@angular/core';
import { LoadingService } from 'src/app/services/loading.service';

@Component({
  selector: 'app-loading',
  templateUrl: './loading.component.html',
  styleUrls: ['./loading.component.css']
})
export class LoadingComponent {
  @Input() message: string = 'Loading...';
  loading$ = this.loadingService.loading$;
  constructor(private loadingService: LoadingService) {}
}