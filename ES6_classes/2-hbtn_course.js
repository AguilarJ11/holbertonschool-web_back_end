export default class HolbertonCourse {
  constructor(name, lenght, students) {
    this._name = name;
    this._lenght = lenght;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    this._name = name;
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(lenght) {
    this._lenght = lenght;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    this._students = students;
  }
}
