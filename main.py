import typing
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware

# 1. DATABASE CONFIGURATION (SQLite)
DATABASE_URL = "sqlite:///./static/Mt"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 2. SQLALCHEMY MODEL
class StudentResultModel(Base):
    __tablename__ = "student_results"

    slno = Column(Integer, primary_key=True, index=True)
    examid = Column(String, nullable=True)
    admitid = Column(String, nullable=True)
    result_status = Column(String, nullable=True)
    candidate_type = Column(String, nullable=True)
    sem1_examid = Column(String, nullable=True)
    sem2_examid = Column(String, nullable=True)
    sem3_examid = Column(String, nullable=True)
    rollno = Column(String, index=True, nullable=True)
    ansidrno = Column(String, nullable=True)
    regno = Column(String, nullable=True)
    semyr_code = Column(String, nullable=True)
    sname = Column(String, nullable=True)
    name_in_hindi = Column(String, nullable=True)
    fname = Column(String, nullable=True)
    mname = Column(String, nullable=True)
    dob = Column(String, nullable=True)
    category = Column(String, nullable=True)
    clrollno = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    stream = Column(String, nullable=True)
    course = Column(String, nullable=True)
    subject = Column(String, index=True, nullable=True)
    spl_group = Column(String, nullable=True)
    college_code = Column(String, nullable=True)
    college_name = Column(String, nullable=True)
    centre_code = Column(String, nullable=True)
    centre_name = Column(String, nullable=True)

    # Semester 1
    s1_paper1c = Column(String, nullable=True)
    s1_paper2c = Column(String, nullable=True)
    s1_paper3c = Column(String, nullable=True)
    s1_paper4c = Column(String, nullable=True)
    s1_papername1 = Column(String, nullable=True)
    s1_papername2 = Column(String, nullable=True)
    s1_papername3 = Column(String, nullable=True)
    s1_papername4 = Column(String, nullable=True)
    s1_pap1int = Column(String, nullable=True)
    s1_pap2int = Column(String, nullable=True)
    s1_pap3int = Column(String, nullable=True)
    s1_pap4int = Column(String, nullable=True)
    s1_pap1th = Column(String, nullable=True)
    s1_pap2th = Column(String, nullable=True)
    s1_pap3th = Column(String, nullable=True)
    s1_pap4th = Column(String, nullable=True)
    s1_pap1tot = Column(String, nullable=True)
    s1_pap2tot = Column(String, nullable=True)
    s1_pap3tot = Column(String, nullable=True)
    s1_pap4tot = Column(String, nullable=True)
    s1_pap1_grade = Column(String, nullable=True)
    s1_pap2_grade = Column(String, nullable=True)
    s1_pap3_grade = Column(String, nullable=True)
    s1_pap4_grade = Column(String, nullable=True)
    s1_total = Column(String, nullable=True)
    s1_result = Column(String, nullable=True)
    s1_grade = Column(String, nullable=True)
    s1_percentage = Column(String, nullable=True)
    s1_sgpa = Column(String, nullable=True)

    # Semester 2
    s2_paper1c = Column(String, nullable=True)
    s2_paper2c = Column(String, nullable=True)
    s2_paper3c = Column(String, nullable=True)
    s2_paper4c = Column(String, nullable=True)
    s2_papername1 = Column(String, nullable=True)
    s2_papername2 = Column(String, nullable=True)
    s2_papername3 = Column(String, nullable=True)
    s2_papername4 = Column(String, nullable=True)
    s2_pap1int = Column(String, nullable=True)
    s2_pap2int = Column(String, nullable=True)
    s2_pap3int = Column(String, nullable=True)
    s2_pap4int = Column(String, nullable=True)
    s2_pap1th = Column(String, nullable=True)
    s2_pap2th = Column(String, nullable=True)
    s2_pap3th = Column(String, nullable=True)
    s2_pap4th = Column(String, nullable=True)
    s2_pap1tot = Column(String, nullable=True)
    s2_pap2tot = Column(String, nullable=True)
    s2_pap3tot = Column(String, nullable=True)
    s2_pap4tot = Column(String, nullable=True)
    s2_pap1_grade = Column(String, nullable=True)
    s2_pap2_grade = Column(String, nullable=True)
    s2_pap3_grade = Column(String, nullable=True)
    s2_pap4_grade = Column(String, nullable=True)
    s2_total = Column(String, nullable=True)
    s2_result = Column(String, nullable=True)
    s2_grade = Column(String, nullable=True)
    s2_percentage = Column(String, nullable=True)
    s2_sgpa = Column(String, nullable=True)

    # Semester 3
    s3_paper1c = Column(String, nullable=True)
    s3_paper2c = Column(String, nullable=True)
    s3_paper3c = Column(String, nullable=True)
    s3_paper4c = Column(String, nullable=True)
    s3_papername1 = Column(String, nullable=True)
    s3_papername2 = Column(String, nullable=True)
    s3_papername3 = Column(String, nullable=True)
    s3_papername4 = Column(String, nullable=True)
    s3_pap1int = Column(String, nullable=True)
    s3_pap2int = Column(String, nullable=True)
    s3_pap3int = Column(String, nullable=True)
    s3_pap4int = Column(String, nullable=True)
    s3_pap1th = Column(String, nullable=True)
    s3_pap2th = Column(String, nullable=True)
    s3_pap3th = Column(String, nullable=True)
    s3_pap4th = Column(String, nullable=True)
    s3_pap1_grade = Column(String, nullable=True)
    s3_pap2_grade = Column(String, nullable=True)
    s3_pap3_grade = Column(String, nullable=True)
    s3_pap4_grade = Column(String, nullable=True)
    s3_pap1tot = Column(String, nullable=True)
    s3_pap2tot = Column(String, nullable=True)
    s3_pap3tot = Column(String, nullable=True)
    s3_pap4tot = Column(String, nullable=True)
    s3_total = Column(String, nullable=True)
    s3_result = Column(String, nullable=True)
    s3_grade = Column(String, nullable=True)
    s3_percentage = Column(String, nullable=True)
    s3_sgpa = Column(String, nullable=True)

    # Semester 4
    s4_paper1c = Column(String, nullable=True)
    s4_paper2c = Column(String, nullable=True)
    s4_paper3c = Column(String, nullable=True)
    s4_paper4c = Column(String, nullable=True)
    s4_papername1 = Column(String, nullable=True)
    s4_papername2 = Column(String, nullable=True)
    s4_papername3 = Column(String, nullable=True)
    s4_papername4 = Column(String, nullable=True)
    s4_pap1int = Column(String, nullable=True)
    s4_pap2int = Column(String, nullable=True)
    s4_pap3int = Column(String, nullable=True)
    s4_pap4int = Column(String, nullable=True)
    s4_pap1th = Column(String, nullable=True)
    s4_pap2th = Column(String, nullable=True)
    s4_pap3th = Column(String, nullable=True)
    s4_pap4th = Column(String, nullable=True)
    s4_pap1tot = Column(String, nullable=True)
    s4_pap2tot = Column(String, nullable=True)
    s4_pap3tot = Column(String, nullable=True)
    s4_pap4tot = Column(String, nullable=True)
    s4_pap1_grade = Column(String, nullable=True)
    s4_pap2_grade = Column(String, nullable=True)
    s4_pap3_grade = Column(String, nullable=True)
    s4_pap4_grade = Column(String, nullable=True)
    s4_total = Column(String, nullable=True)
    s4_result = Column(String, nullable=True)
    s4_grade = Column(String, nullable=True)
    s4_percentage = Column(String, nullable=True)
    s4_sgpa = Column(String, nullable=True)

    # Final & Metadata
    f_total = Column(String, nullable=True)
    f_percentage = Column(String, nullable=True)
    f_grade = Column(String, nullable=True)
    f_cgpa = Column(String, nullable=True)
    f_sgpa = Column(String, nullable=True)
    f_division = Column(String, nullable=True)
    f_remarks = Column(String, nullable=True)
    marksheetno = Column(String, nullable=True)
    provisionalno = Column(String, nullable=True)
    held_month = Column(String, nullable=True)
    held_year = Column(String, nullable=True)
    date_publication = Column(String, nullable=True)
    download_count = Column(Integer, nullable=True, default=0)
    coursename = Column(String, nullable=True)
    sassion = Column(String, nullable=True)
    honours = Column(String, nullable=True)
    held_year_1 = Column(String, nullable=True)
    total = Column(String, nullable=True)
    result = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)


# 3. PYDANTIC SCHEMAS
class StudentResultSchema(BaseModel):
    slno: int
    examid: Optional[str] = None
    admitid: Optional[str] = None
    result_status: Optional[str] = None
    candidate_type: Optional[str] = None
    sem1_examid: Optional[str] = None
    sem2_examid: Optional[str] = None
    sem3_examid: Optional[str] = None
    rollno: Optional[str] = None
    ansidrno: Optional[str] = None
    regno: Optional[str] = None
    semyr_code: Optional[str] = None
    sname: Optional[str] = None
    name_in_hindi: Optional[str] = None
    fname: Optional[str] = None
    mname: Optional[str] = None
    dob: Optional[str] = None
    category: Optional[str] = None
    clrollno: Optional[str] = None
    gender: Optional[str] = None
    stream: Optional[str] = None
    course: Optional[str] = None
    subject: Optional[str] = None
    spl_group: Optional[str] = None
    college_code: Optional[str] = None
    college_name: Optional[str] = None
    centre_code: Optional[str] = None
    centre_name: Optional[str] = None

    # Semester 1
    s1_paper1c: Optional[str] = None
    s1_paper2c: Optional[str] = None
    s1_paper3c: Optional[str] = None
    s1_paper4c: Optional[str] = None
    s1_papername1: Optional[str] = None
    s1_papername2: Optional[str] = None
    s1_papername3: Optional[str] = None
    s1_papername4: Optional[str] = None
    s1_pap1int: Optional[str] = None
    s1_pap2int: Optional[str] = None
    s1_pap3int: Optional[str] = None
    s1_pap4int: Optional[str] = None
    s1_pap1th: Optional[str] = None
    s1_pap2th: Optional[str] = None
    s1_pap3th: Optional[str] = None
    s1_pap4th: Optional[str] = None
    s1_pap1tot: Optional[str] = None
    s1_pap2tot: Optional[str] = None
    s1_pap3tot: Optional[str] = None
    s1_pap4tot: Optional[str] = None
    s1_pap1_grade: Optional[str] = None
    s1_pap2_grade: Optional[str] = None
    s1_pap3_grade: Optional[str] = None
    s1_pap4_grade: Optional[str] = None
    s1_total: Optional[str] = None
    s1_result: Optional[str] = None
    s1_grade: Optional[str] = None
    s1_percentage: Optional[str] = None
    s1_sgpa: Optional[str] = None

    # Semester 2
    s2_paper1c: Optional[str] = None
    s2_paper2c: Optional[str] = None
    s2_paper3c: Optional[str] = None
    s2_paper4c: Optional[str] = None
    s2_papername1: Optional[str] = None
    s2_papername2: Optional[str] = None
    s2_papername3: Optional[str] = None
    s2_papername4: Optional[str] = None
    s2_pap1int: Optional[str] = None
    s2_pap2int: Optional[str] = None
    s2_pap3int: Optional[str] = None
    s2_pap4int: Optional[str] = None
    s2_pap1th: Optional[str] = None
    s2_pap2th: Optional[str] = None
    s2_pap3th: Optional[str] = None
    s2_pap4th: Optional[str] = None
    s2_pap1tot: Optional[str] = None
    s2_pap2tot: Optional[str] = None
    s2_pap3tot: Optional[str] = None
    s2_pap4tot: Optional[str] = None
    s2_pap1_grade: Optional[str] = None
    s2_pap2_grade: Optional[str] = None
    s2_pap3_grade: Optional[str] = None
    s2_pap4_grade: Optional[str] = None
    s2_total: Optional[str] = None
    s2_result: Optional[str] = None
    s2_grade: Optional[str] = None
    s2_percentage: Optional[str] = None
    s2_sgpa: Optional[str] = None

    # Semester 3
    s3_paper1c: Optional[str] = None
    s3_paper2c: Optional[str] = None
    s3_paper3c: Optional[str] = None
    s3_paper4c: Optional[str] = None
    s3_papername1: Optional[str] = None
    s3_papername2: Optional[str] = None
    s3_papername3: Optional[str] = None
    s3_papername4: Optional[str] = None
    s3_pap1int: Optional[str] = None
    s3_pap2int: Optional[str] = None
    s3_pap3int: Optional[str] = None
    s3_pap4int: Optional[str] = None
    s3_pap1th: Optional[str] = None
    s3_pap2th: Optional[str] = None
    s3_pap3th: Optional[str] = None
    s3_pap4th: Optional[str] = None
    s3_pap1_grade: Optional[str] = None
    s3_pap2_grade: Optional[str] = None
    s3_pap3_grade: Optional[str] = None
    s3_pap4_grade: Optional[str] = None
    s3_pap1tot: Optional[str] = None
    s3_pap2tot: Optional[str] = None
    s3_pap3tot: Optional[str] = None
    s3_pap4tot: Optional[str] = None
    s3_total: Optional[str] = None
    s3_result: Optional[str] = None
    s3_grade: Optional[str] = None
    s3_percentage: Optional[str] = None
    s3_sgpa: Optional[str] = None

    # Semester 4
    s4_paper1c: Optional[str] = None
    s4_paper2c: Optional[str] = None
    s4_paper3c: Optional[str] = None
    s4_paper4c: Optional[str] = None
    s4_papername1: Optional[str] = None
    s4_papername2: Optional[str] = None
    s4_papername3: Optional[str] = None
    s4_papername4: Optional[str] = None
    s4_pap1int: Optional[str] = None
    s4_pap2int: Optional[str] = None
    s4_pap3int: Optional[str] = None
    s4_pap4int: Optional[str] = None
    s4_pap1th: Optional[str] = None
    s4_pap2th: Optional[str] = None
    s4_pap3th: Optional[str] = None
    s4_pap4th: Optional[str] = None
    s4_pap1tot: Optional[str] = None
    s4_pap2tot: Optional[str] = None
    s4_pap3tot: Optional[str] = None
    s4_pap4tot: Optional[str] = None
    s4_pap1_grade: Optional[str] = None
    s4_pap2_grade: Optional[str] = None
    s4_pap3_grade: Optional[str] = None
    s4_pap4_grade: Optional[str] = None
    s4_total: Optional[str] = None
    s4_result: Optional[str] = None
    s4_grade: Optional[str] = None
    s4_percentage: Optional[str] = None
    s4_sgpa: Optional[str] = None

    # Final & Metadata
    f_total: Optional[str] = None
    f_percentage: Optional[str] = None
    f_grade: Optional[str] = None
    f_cgpa: Optional[str] = None
    f_sgpa: Optional[str] = None
    f_division: Optional[str] = None
    f_remarks: Optional[str] = None
    marksheetno: Optional[str] = None
    provisionalno: Optional[str] = None
    held_month: Optional[str] = None
    held_year: Optional[str] = None
    date_publication: Optional[str] = None
    download_count: Optional[int] = 0
    coursename: Optional[str] = None
    sassion: Optional[str] = None
    honours: Optional[str] = None
    held_year_1: Optional[str] = None
    total: Optional[str] = None
    result: Optional[str] = None

    class Config:
        from_attributes = True


# 4. FASTAPI APP & DEPENDENCY

app = FastAPI(title="Student Result Management API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000/",
        "http://127.0.0.1:5500",# VS Code Live Server
        ""https://npupgresult.blogspot.com/""  # Production URL
    ],
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE sabhi methods allow honge
    allow_headers=["*"],  # Sabhi request headers allow honge
)


# ----------------- STATIC FILES MOUNT KAREIN -----------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates directory specify karein
templates = Jinja2Templates(directory="templates")


# ----------------- HOME / INDEX ROUTE -----------------
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 5. EXISTING ENDPOINTS


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 5. EXISTING ENDPOINTS


@app.post(
    "/results/", response_model=StudentResultSchema, status_code=status.HTTP_201_CREATED
)
def create_student_result(record: StudentResultSchema, db: Session = Depends(get_db)):
    db_record = (
        db.query(StudentResultModel)
        .filter(StudentResultModel.slno == record.slno)
        .first()
    )
    if db_record:
        return JSONResponse(
            status_code=400,
            content={
                "insurt": False,
                "detail": f"Record with slno {record.slno} already exists.",
            },
        )
        # raise HTTPException(
        #     status_code=400,
        #     insurt=False,
        #     detail=f"Record with slno {record.slno} already exists.",
        # )

    new_record = StudentResultModel(**record.model_dump())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


@app.get("/results/", response_model=List[StudentResultSchema])
def get_all_results(skip: int = 0, limit: int = 50000, db: Session = Depends(get_db)):
    return db.query(StudentResultModel).offset(skip).limit(limit).all()


@app.get("/results/{slno}", response_model=StudentResultSchema)
def get_result_by_slno(slno: int, db: Session = Depends(get_db)):
    record = (
        db.query(StudentResultModel).filter(StudentResultModel.slno == slno).first()
    )
    if not record:
        raise HTTPException(status_code=404, detail="Student record not found")
    return record


@app.get("/results/rollno/{rollno}", response_model=StudentResultSchema)
def get_result_by_rollno(rollno: str, db: Session = Depends(get_db)):
    record = (
        db.query(StudentResultModel).filter(StudentResultModel.rollno == rollno).first()
    )
    if not record:
        raise HTTPException(
            status_code=404, detail="Record not found for this roll number"
        )
    return record


# ALL SUBJECT TOPPERS IN A SINGLE DICTIONARY
@app.get("/toppers")
def get_all_subject_toppers(db: Session = Depends(get_db)):
    """
    Har ek subject ka topper (highest s3_percentage) nikal kar
    { "Botany": {...student_data...}, "Chemistry": {...student_data...} }
    format me return karta hai.
    """
    # 1. Sabhi unique subjects nikalen
    distinct_subjects = db.query(StudentResultModel.subject).distinct().all()
    subjects = [s[0] for s in distinct_subjects if s[0]]

    if not subjects:
        raise HTTPException(
            status_code=404, detail="Database me koi subject nahi mila."
        )

    toppers_summary = {}

    # 2. Har subject ke highest s3_percentage waale student ko fetch karein
    for subj in subjects:
        top_student = (
            db.query(StudentResultModel)
            .filter(StudentResultModel.subject == subj)
            .order_by(func.cast(StudentResultModel.s3_percentage, Float).desc())
            .first()
        )
        if top_student:
            toppers_summary[subj] = StudentResultSchema.model_validate(top_student)

    return toppers_summary


# 6. NEW SUBJECT-BASED ENDPOINTS (3 New Methods)


# METHOD 1: Subject wise Topper (Highest s3_percentage wala student)
@app.get("/toppers/subject/{subject_name}", response_model=StudentResultSchema)
def get_subject_topper_s3(subject_name: str, db: Session = Depends(get_db)):
    """
    Ek specific subject ke andar jis student ki s3_percentage sabse zyada (highest)
    hai, use return karega.
    """
    # SQLite me s3_percentage string format me ho sakta hai, isliye CAST karke Float me convert kar rahe hain
    topper = (
        db.query(StudentResultModel)
        .filter(func.lower(StudentResultModel.subject) == subject_name.lower())
        .order_by(func.cast(StudentResultModel.s3_percentage, Float).desc())
        .first()
    )

    if not topper:
        raise HTTPException(
            status_code=404, detail=f"No student found for subject: {subject_name}"
        )

    return topper


# METHOD 2: Subject wise All Students (Ek subject ke saare students)
@app.get("/students/subject/{subject_name}", response_model=List[StudentResultSchema])
def get_all_students_by_subject(
    subject_name: str, skip: int = 0, limit: int = 50000, db: Session = Depends(get_db)
):
    """
    Ek specific subject ke sabhi students ki list return karega.
    """
    students = (
        db.query(StudentResultModel)
        .filter(func.lower(StudentResultModel.subject) == subject_name.lower())
        .offset(skip)
        .limit(limit)
        .all()
    )
    # print(topper)

    if not students:
        raise HTTPException(
            status_code=404, detail=f"No students found for subject: {subject_name}"
        )

    return students


# METHOD 3: Get List of All Unique Subjects
@app.get("/subjects/", response_model=List[str])
def get_all_unique_subjects(db: Session = Depends(get_db)):
    """
    Database me jitne bhi unique subjects hain, unki list return karega.
    """
    results = db.query(StudentResultModel.subject).distinct().all()
    subjects = [row[0] for row in results if row[0] is not None]

    if not subjects:
        raise HTTPException(status_code=404, detail="No subjects found in database")

    return subjects


# python -m uvicorn main:app --reload
