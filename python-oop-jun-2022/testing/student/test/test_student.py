import unittest
from unittest import TestCase

from project.student import Student


class StudentTest(TestCase):
    NAME = 'Student'

    def setUp(self) -> None:
        self.student = Student(self.NAME)

    def test_student_init_without_courses(self):
        self.assertEqual(self.student.name, self.NAME)
        self.assertDictEqual({}, self.student.courses)

    def test_student_init_with_courses(self):
        courses = {'Python Advanced': ['note1', 'note2', 'note3']}
        student = Student(self.NAME, courses)
        self.assertEqual(student.name, self.NAME)
        self.assertDictEqual(student.courses, courses)

    def test_enroll_updates_existing_course_with_course_notes(self):
        course_name = 'Python Advanced'
        notes = ['note1', 'note2', 'note3']
        courses = {course_name: notes}

        student = Student(self.NAME, courses)
        student.courses = {course_name: []}

        expected_result = "Course already added. Notes have been updated."
        actual_result = student.enroll(course_name, notes)

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(student.courses[course_name], ['note1', 'note2', 'note3'])

    def test_enroll_add_course_notes_with_y(self):
        course_name = 'Python Advanced'
        notes = ['note4', 'note5']
        actual_result = self.student.enroll(course_name, notes, "Y")
        expected_result = "Course and course notes have been added."
        expected_courses = {course_name: notes}
        self.assertEqual(actual_result, expected_result)
        self.assertDictEqual(self.student.courses, expected_courses)

    def test_enroll_add_course_notes_with_empty_string(self):
        course_name = 'Python Advanced'
        notes = ['note4', 'note5']
        actual_result = self.student.enroll(course_name, notes, "")
        expected_result = "Course and course notes have been added."
        expected_courses = {course_name: notes}
        self.assertEqual(actual_result, expected_result)
        self.assertDictEqual(self.student.courses, expected_courses)

    def test_enroll_add_course_expect_to_be_added_without_notes(self):
        course_name = 'Python OOP'
        result = self.student.enroll(course_name, ['note1'], "N")
        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(self.student.courses[course_name], [])

    def test_add_missing_course_with_empty_notes(self):
        course_name = 'Python OOP'
        notes = []
        actual_result = self.student.enroll(course_name, notes, "N")
        actual_dict = self.student.courses
        expected_dict = {course_name: []}
        expected_message = "Course has been added."
        self.assertEqual(expected_message, actual_result)
        self.assertDictEqual(actual_dict, expected_dict)

    def test_add_notes_to_missing_course_expect_raise(self):
        course_name = 'JS Advanced'
        notes = ['note1', 'note2']

        with self.assertRaises(Exception) as error:
            self.student.add_notes(course_name, notes)
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_add_notes_to_existing_course_expect_to_be_added(self):
        course_name = 'Python Advanced'
        notes = []
        student = Student(self.NAME, {course_name: []})

        result = student.add_notes(course_name, 'note1')
        expected_message = "Notes have been updated"
        self.assertEqual(expected_message, result)
        self.assertListEqual(student.courses[course_name], ['note1'])

    def test_leave_course_with_invalid_course_name_raise(self):
        course_name = 'Python Advanced'

        with self.assertRaises(Exception) as error:
            self.student.leave_course(course_name)

        expected_message = "Cannot remove course. Course not found."

        self.assertEqual(expected_message, str(error.exception))

    def test_leave_course_with_valid_course_in_student_courses(self):
        course_name = 'Python Advanced'
        self.student.enroll(course_name, [], "N")

        result = self.student.leave_course(course_name)

        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in self.student.courses)


if __name__ == '__main__':
    unittest.main()
