export default function getListStudents() {
    function student(id, firstname, location) {
        this.id = id
        this.firstname = firstname
        this.location = location
    };
    const students = []
    const Guillaume = new student(1, 'Guillaume', 'San Francisco')
    const Jamese = new student(2, 'James', 'Columbia')
    const Serena = new student(5, 'Serena', 'San Francisco')
    students.push(Guillaume, Jamese, Serena)

    return students
}