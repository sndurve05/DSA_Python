class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        from collections import deque 
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students and sandwiches:
            sw = sandwiches[0]
            if sw not in students:
                break
            stu = students.popleft()
         
            if stu == sw:
                sandwiches.popleft()
            else:
                students.append(stu)

        return len(students)