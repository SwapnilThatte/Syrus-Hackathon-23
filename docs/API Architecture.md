# API Design

<hr>

# Auth API

## "/auth/register/worker" [POST] 
#### Required 
- Name 
- Age 
- Password 
- Gender
- Email 
- Profile_photo_URL
- Phone_number,
- Address 
- Aadhar_URL, 
- City_of_origin, 
- Medical_history, 
- Pregnancy_status, 
- Prefered_work_location,  
- Skills, 
- Languages, 
- All_jobs_applied, 
- Worker_rating, 
- JobsApplied

<hr>

## "/auth/register/employer" [POST]
@Required \
{Name, Password, Email, Profile_photo_URL, Phone_number}

<hr>

## "/auth/login/worker" [POST]
@Required \
{Phone_number, password}

<hr>

## "/auth/login/employer" [POST]
@Required \
{Phone_number, password}

<hr>

## "/worker/feed/:id" [GET]

<hr>

# Worker API

## "/worker/serarch" [POST]
#### Required  
- Language_preference 
- Wages_per_hours
- Contract_tenure 
- required_skills
- Applicants

<hr>

## "/worker/view/job/:jobid" [POST]
#### Required
- workerID

<hr>

## "worker/view/employer/:employerid" [POST]
#### Required
- wokerid

<hr>

## "worker/complaints/new" [POST]
#### Required
- complaint_of => employerid
- Complaint_description =
<hr>

## "worker/view/complaints/:workerid" [GET]



# Employer API