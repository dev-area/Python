import { Component } from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/map';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private _http:Http) {
    this.c1.name = "eli"
   }
  title = 'app';
  c1:Cust = new Cust();
  click1(){
    this.getAllBooks().subscribe(b => this.c1 = b)
  }

  getAllBooks()
  {
    return this._http
          .get("./getcust")
          .map(r => <Cust>r.json())

  }

}

export class Cust{
    name:string;
    age:number;
    city:string;
}
