import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-confirmation-dialog',
  template: `
    <h2 mat-dialog-title>{{ data.title }}</h2>
    <mat-dialog-content>{{ data.message }}</mat-dialog-content>
    <mat-dialog-actions class="d-flex justify-content-end">
      <button mat-button (click)="onNo()">Cancel</button>
      <button mat-raised-button color="warn" (click)="onYes()">Confirm</button>
    </mat-dialog-actions>
  `
})
export class ConfirmationDialogComponent {
  constructor(
    @Inject(MAT_DIALOG_DATA) public data: { title: string, message: string },
    private dialogRef: MatDialogRef<ConfirmationDialogComponent>
  ) {}

  onYes() { this.dialogRef.close(true); }
  onNo() { this.dialogRef.close(false); }
}
