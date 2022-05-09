import { Component, OnInit, Input, HostBinding } from '@angular/core';

import { Router } from '@angular/router';
import { Course } from '../models';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  host: {class: 'mb-3 ms-3 me-3'},
  styleUrls: ['./course-card.component.css']
})
export class CourseCardComponent implements OnInit {
  @Input() course: Course | undefined;
  @Input() card: boolean = true;
  @HostBinding('class.col') classCol: boolean = false;

  constructor(
    private router: Router
  ) { }

  ngOnInit(): void {
    if (this.card) {
      this.classCol = true;
    }
  }

  navigateToCourseDetail(): void {
    if (this.course?.id)
      this.router.navigate([`/course-detail/${this.course?.id}`]);
  }
}