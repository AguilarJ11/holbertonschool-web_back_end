export default class HolbertonCourse {
  constructor(name, lenght, students) {
    this.name = name
    this.lenght = lenght;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === String) {    
        this._name = name;
    }
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(lenght) {
    if (typeof length === Number) {
        this._lenght = lenght;
    }
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (Array.isArray(students) && students.every(elem => typeof elem === String)) {
        this._students = students;
    }
  }
}
