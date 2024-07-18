from fastapi import APIRouter, HTTPException
import requests

# Helper function to get the access token for the OneRoster API
def get_access_token():
    """
    Retrieves the access token required for authenticating API requests to the OneRoster API.
    
    Returns:
        str: The access token.
    
    Raises:
        HTTPException: If the access token could not be obtained.
    """
    token_url = 'https://demo.aeries.net/aeries/token'
    client_id = '1279e5c6b747b6d62b7c76db3a205d40eb7458e678a90493d537d5af6b953550'
    client_secret = '68019dbf8d8ba82980dd148eecc3977ac0d7f1f040d444225874c88eb80b9c1a'
    auth = (client_id, client_secret)
    
    response = requests.post(token_url, auth=auth)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to obtain access token")

# Endpoint Classes       
class AcademicSessions:
    """
    Class for handling API routes related to academic sessions.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/{id}", self.get_session_info, methods=["GET"])

    def get_session_info(self, id: str):
        """
        Retrieves information for a specific academic session by its ID.
        
        Args:
            id (str): The ID of the academic session.
        
        Returns:
            dict: The academic session information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/academicSessions/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'session data for id: {id} missing or not found'}

class Classes:
    """
    Class for handling API routes related to classes.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_class_info, methods=["GET"])
        self.router.add_api_route("/{class_id}", self.get_class_info_with_id, methods=["GET"])
        self.router.add_api_route("/{class_id}/students", self.get_students_by_class, methods=["GET"])
        self.router.add_api_route("/{class_id}/teachers", self.get_teachers_by_class, methods=["GET"])
    
    def get_class_info(self):
        """
        Retrieves information for all classes.
        
        Returns:
            dict: The classes information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/classes'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})

        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_class_info_with_id(self, class_id: str):
        """
        Retrieves information for a specific class by its ID.
        
        Args:
            class_id (str): The ID of the class.
        
        Returns:
            dict: The class information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/classes/{class_id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})

        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'class data for id: {class_id} missing or not found'}
    
    def get_students_by_class(self, class_id: str):
        """
        Retrieves the list of students for a specific class by its ID.
        
        Args:
            class_id (str): The ID of the class.
        
        Returns:
            dict: The students information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/classes/{class_id}/students'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'students for class id: {class_id} missing or not found'}
    
    def get_teachers_by_class(self, class_id: str):
        """
        Retrieves the list of teachers for a specific class by its ID.
        
        Args:
            class_id (str): The ID of the class.
        
        Returns:
            dict: The teachers information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/classes/{class_id}/teachers'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})

        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'teachers for class id: {class_id} missing or not found'}

class Courses:
    """
    Class for handling API routes related to courses.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_courses, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_courses_by_id, methods=["GET"])
        self.router.add_api_route("/{course_id}/classes", self.get_classes_by_course, methods=["GET"])

    def get_courses(self):
        """
        Retrieves information for all courses.
        
        Returns:
            dict: The courses information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/courses'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}
        
    def get_courses_by_id(self, id: str):
        """
        Retrieves information for a specific course by its ID.
        
        Args:
            id (str): The ID of the course.
        
        Returns:
            dict: The course information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/courses/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}
    
    def get_classes_by_course(self, course_id: str):
        """
        Retrieves the list of classes for a specific course by its ID.
        
        Args:
            course_id (str): The ID of the course.
        
        Returns:
            dict: The classes information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/courses/{course_id}/classes'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'classes for course id: {course_id} missing or not found'}

class Demographics:
    """
    Class for handling API routes related to demographics.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_demographics, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_demographic_by_id, methods=["GET"])

    def get_demographics(self):
        """
        Retrieves demographic information for all entities.
        
        Returns:
            dict: The demographic information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/demographics'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_demographic_by_id(self, id: str):
        """
        Retrieves demographic information for a specific entity by its ID.
        
        Args:
            id (str): The ID of the entity.
        
        Returns:
            dict: The demographic information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/demographics/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}

class Enrollments:
    """
    Class for handling API routes related to enrollments.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_enrollments, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_enrollment_by_id, methods=["GET"])

    def get_enrollments(self):
        """
        Retrieves enrollment information for all entities.
        
        Returns:
            dict: The enrollment information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/enrollments'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_enrollment_by_id(self, id: str):
        """
        Retrieves enrollment information for a specific entity by its ID.
        
        Args:
            id (str): The ID of the entity.
        
        Returns:
            dict: The enrollment information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/enrollments/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}

class GradingPeriods:
    """
    Class for handling API routes related to grading periods.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_grading_periods, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_grading_period_by_id, methods=["GET"])

    def get_grading_periods(self):
        """
        Retrieves information for all grading periods.
        
        Returns:
            dict: The grading periods information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/gradingPeriods'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_grading_period_by_id(self, id: str):
        """
        Retrieves information for a specific grading period by its ID.
        
        Args:
            id (str): The ID of the grading period.
        
        Returns:
            dict: The grading period information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/gradingPeriods/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}

class Orgs:
    """
    Class for handling API routes related to organizations.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_orgs, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_org_by_id, methods=["GET"])

    def get_orgs(self):
        """
        Retrieves information for all organizations.
        
        Returns:
            dict: The organizations information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/orgs'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_org_by_id(self, id: str):
        """
        Retrieves information for a specific organization by its ID.
        
        Args:
            id (str): The ID of the organization.
        
        Returns:
            dict: The organization information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/orgs/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}

class Schools:
    """
    Class for handling API routes related to schools.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_schools, methods=["GET"])
        self.router.add_api_route("/{school_id}", self.get_school_by_id, methods=["GET"])
        self.router.add_api_route("/{school_id}/classes", self.get_classes, methods=["GET"])
        self.router.add_api_route("/{school_id}/classes/{class_id}/enrollments", self.get_enrollment_by_school_and_class, methods=["GET"])
        self.router.add_api_route("/{school_id}/classes/{class_id}/students", self.get_students_by_school_and_class, methods=["GET"])
        self.router.add_api_route("/{school_id}/classes/{class_id}/teachers", self.get_teachers_by_school_and_class, methods=["GET"])
        self.router.add_api_route("/{school_id}/enrollments", self.get_enrollments_by_school, methods=["GET"])
        self.router.add_api_route("/{school_id}/students", self.get_students_by_school, methods=["GET"])
        self.router.add_api_route("/{school_id}/teachers", self.get_teachers_by_school, methods=["GET"])
        self.router.add_api_route("/{school_id}/terms", self.get_terms, methods=["GET"])

    def get_schools(self):
        """
        Retrieves information for all schools.
        
        Returns:
            dict: The schools information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_school_by_id(self, school_id: str):
        """
        Retrieves information for a specific school by its ID.
        
        Args:
            school_id (str): The ID of the school.
        
        Returns:
            dict: The school information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {school_id} missing or not found'}

    def get_classes(self, school_id: str):
        """
        Retrieves the list of classes for a specific school by its ID.
        
        Args:
            school_id (str): The ID of the school.
        
        Returns:
            dict: The classes information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/classes'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_enrollment_by_school_and_class(self, school_id: str, class_id: str):
        """
        Retrieves the list of enrollments for a specific class in a specific school.
        
        Args:
            school_id (str): The ID of the school.
            class_id (str): The ID of the class.
        
        Returns:
            dict: The enrollments information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/classes/{class_id}/enrollments'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_students_by_school_and_class(self, school_id: str, class_id: str):
        """
        Retrieves the list of students for a specific class in a specific school.
        
        Args:
            school_id (str): The ID of the school.
            class_id (str): The ID of the class.
        
        Returns:
            dict: The students information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/classes/{class_id}/students'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_teachers_by_school_and_class(self, school_id: str, class_id: str):
        """
        Retrieves the list of teachers for a specific class in a specific school.
        
        Args:
            school_id (str): The ID of the school.
            class_id (str): The ID of the class.
        
        Returns:
            dict: The teachers information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/classes/{class_id}/teachers'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_enrollments_by_school(self, school_id: str):
        """
        Retrieves the list of enrollments for a specific school by its ID.
        
        Args:
            school_id (str): The ID of the school.
        
        Returns:
            dict: The enrollments information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/enrollments'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_students_by_school(self, school_id: str):
        """
        Retrieves the list of students for a specific school by its ID.
        
        Args:
            school_id (str): The ID of the school.
        
        Returns:
            dict: The students information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/students'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_teachers_by_school(self, school_id: str):
        """
        Retrieves the list of teachers for a specific school by its ID.
        
        Args:
            school_id (str): The ID of the school.
        
        Returns:
            dict: The teachers information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/teachers'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_terms(self, school_id: str):
        """
        Retrieves the list of terms for a specific school by its ID.
        
        Args:
            school_id (str): The ID of the school.
        
        Returns:
            dict: The terms information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/schools/{school_id}/terms'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

class Students:
    """
    Class for handling API routes related to students.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_students, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_student_by_id, methods=["GET"])
        self.router.add_api_route("/{student_id}/classes", self.get_student_classes, methods=["GET"])

    def get_students(self):
        """
        Retrieves information for all students.
        
        Returns:
            dict: The students information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/students'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_student_by_id(self, id: str):
        """
        Retrieves information for a specific student by their ID.
        
        Args:
            id (str): The ID of the student.
        
        Returns:
            dict: The student information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/students/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}
    
    def get_student_classes(self, student_id: str):
        """
        Retrieves the list of classes for a specific student by their ID.
        
        Args:
            student_id (str): The ID of the student.
        
        Returns:
            dict: The classes information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/students/{student_id}/classes'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'classes for student id: {student_id} missing or not found'}

class Teachers:
    """
    Class for handling API routes related to teachers.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_teachers, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_teacher_by_id, methods=["GET"])
        self.router.add_api_route("/{teacher_id}/classes", self.get_teacher_classes, methods=["GET"])
    
    def get_teachers(self):
        """
        Retrieves information for all teachers.
        
        Returns:
            dict: The teachers information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/teachers'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_teacher_by_id(self, id: str):
        """
        Retrieves information for a specific teacher by their ID.
        
        Args:
            id (str): The ID of the teacher.
        
        Returns:
            dict: The teacher information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/teachers/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}
    
    def get_teacher_classes(self, teacher_id: str):
        """
        Retrieves the list of classes for a specific teacher by their ID.
        
        Args:
            teacher_id (str): The ID of the teacher.
        
        Returns:
            dict: The classes information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/teachers/{teacher_id}/classes'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'classes for teacher id: {teacher_id} missing or not found'}

class Terms:
    """
    Class for handling API routes related to terms.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_terms, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_term_by_id, methods=["GET"])
        self.router.add_api_route("/{term_id}/classes", self.get_classes_by_term, methods=["GET"])
    
    def get_terms(self):
        """
        Retrieves information for all terms.
        
        Returns:
            dict: The terms information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/terms'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_term_by_id(self, id: str):
        """
        Retrieves information for a specific term by its ID.
        
        Args:
            id (str): The ID of the term.
        
        Returns:
            dict: The term information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/terms/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}

    def get_classes_by_term(self, term_id: str):
        """
        Retrieves the list of classes for a specific term by its ID.
        
        Args:
            term_id (str): The ID of the term.
        
        Returns:
            dict: The classes information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/terms/{term_id}/classes'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'classes for term id: {term_id} missing or not found'}

class Users:
    """
    Class for handling API routes related to users.
    """
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_users, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_user_by_id, methods=["GET"])
        self.router.add_api_route("/{user_id}/classes}", self.get_user_classes, methods=["GET"])
    
    def get_users(self):
        """
        Retrieves information for all users.
        
        Returns:
            dict: The users information.
        """
        url = 'https://demo.aeries.net/aeries/ims/oneroster/v1p1/users'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': 'data not found'}

    def get_user_by_id(self, id: str):
        """
        Retrieves information for a specific user by their ID.
        
        Args:
            id (str): The ID of the user.
        
        Returns:
            dict: The user information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/users/{id}'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'data for id: {id} missing or not found'}
    
    def get_user_classes(self, user_id: str):
        """
        Retrieves the list of classes for a specific user by their ID.
        
        Args:
            user_id (str): The ID of the user.
        
        Returns:
            dict: The classes information.
        """
        url = f'https://demo.aeries.net/aeries/ims/oneroster/v1p1/users/{user_id}/classes'
        response = requests.get(url, headers={'Authorization': f'Bearer {get_access_token()}'})
        if response.status_code == 200:
            return response.json()
        else:
            return {'message': f'classes for user id: {user_id} missing or not found'}