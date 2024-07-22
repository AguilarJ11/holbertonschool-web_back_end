export default class HolbertonCourse {
  constructor(name, lenght, students) {
    this.name = name;
    this.lenght = lenght;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    }
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(lenght) {
    if (typeof lenght === 'number') {
      this._lenght = lenght;
    }
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (
      Array.isArray(students) && students.every((elem) => typeof elem === 'string')
    ) {
      this._students = students;
    }
  }
}
