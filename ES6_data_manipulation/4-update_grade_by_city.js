export default function updateStudentGradeByCity(array, city, newGrades) {
  let stdArray = [];
  stdArray = array
    .filter((students) => students.location === city)
    .map((students) => {
      if (students.id === newGrades.studentId) {
        students.grade = newGrades.grade;
      } else {
        students.grade = 'N/A';
      }
      return students
    });
    return stdArray;
}
