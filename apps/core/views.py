from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Zecpath Day 6 Database Schema",
        "status": "working"
    })


def schema_info(request):
    return JsonResponse({
        "entities": [
            "User",
            "Employer",
            "Candidate",
            "Job",
            "Application"
        ],
        "relationships": {
            "User_to_Employer": "OneToOne",
            "User_to_Candidate": "OneToOne",
            "Employer_to_Job": "OneToMany",
            "Job_to_Application": "OneToMany",
            "Candidate_to_Application": "OneToMany"
        }
    })