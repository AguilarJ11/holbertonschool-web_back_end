export default function getListStudents() {
  function Students(id, firstname, location) {
    this.id = id;
    this.firstname = firstname;
    this.location = location;
  }
  const students = [];
  const Guillaume = new Students(1, 'Guillaume', 'San Francisco');
  const Jamese = new Students(2, 'James', 'Columbia');
  const Serena = new Students(5, 'Serena', 'San Francisco');
  students.push(Guillaume, Jamese, Serena);

  return students;
}
