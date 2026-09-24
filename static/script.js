class StudentAPI {
    constructor(baseURL = location.origin) {
        this.baseURL = baseURL;
    }

    // Common Helper Method (Response Handling & Error Check)
    async _request(endpoint, options = {}) {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, options);
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || `HTTP Error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`API Error on ${endpoint}:`, error.message);
            throw error;
        }
    }

    // 1. INSERT / CREATE NEW STUDENT
    async createStudent(studentData) {
        return await this._request("/results/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(studentData)
        });
    }

    // 2. GET ALL STUDENTS (Pagination ke sath)
    async getAllStudents(skip = 0, limit = 10) {
        return await this._request(`/results/?skip=${skip}&limit=${limit}`);
    }

    // 3. GET SINGLE STUDENT BY SERIAL NO (slno)
    async getStudentBySlno(slno) {
        return await this._request(`/results/${slno}`);
    }

    // 4. GET SINGLE STUDENT BY ROLL NO
    async getStudentByRollNo(rollno) {
        return await this._request(`/results/rollno/${rollno}`);
    }

    // 5. GET ALL SUBJECT TOPPERS (Subhi subjects ke toppers ek dictionary me)
    async getAllSubjectToppers() {
        return await this._request("/toppers");
    }

    // 6. GET TOPPER FOR A SPECIFIC SUBJECT
    async getTopperBySubject(subjectName) {
        return await this._request(`/toppers/subject/${encodeURIComponent(subjectName)}`);
    }

    // 7. GET ALL STUDENTS BY SUBJECT
    async getStudentsBySubject(subjectName, skip = 0, limit = 5000) {
        return await this._request(`/students/subject/${encodeURIComponent(subjectName)}?skip=${skip}&limit=${limit}`);
    }

    // 8. GET LIST OF ALL UNIQUE SUBJECTS
    async getAllSubjects() {
        return await this._request("/subjects/");
    }
}

const e = (t, cl, x) => { let a = document.createElement(t); a.className = cl || ""; a.textContent = x ?? ""; return a; },
    bc = () => {
        history.back();
    },
    rp = (d) => {
        const c = e("div");
        if (!d) return confirm("Student Not Found") && bc();
        c.id = "studentResult";
        document.body.appendChild(c);
        const v = x => x == null || x === "" ? "-" : String(x).trim();
        c.appendChild(e("h2", "result-title", "Student Result Details"));

        console.log(d);


        // Student Details
        let s = e("div", "result-section");
        s.appendChild(e("h3", "section-title", "Student Details"));

        let t = e("table", "result-table");

        [
            ["Name", d.sname],
            ["Father", d.fname], ["Mother", d.mname],
            ["DOB", d.dob], ["Gender", d.gender],
            ["Category", d.category], ["Reg. No.", d.regno],
            ["Roll No.", d.rollno], ["Admit ID", d.admitid],
            ["Candidate", d.candidate_type], ["Class Roll", d.clrollno],
            ["Course", d.coursename], ["Stream", d.stream],
            ["Subject", d.subject], ["Honours", d.honours],
            ["Session", d.sassion], ["College", d.college_name],
            ["College Code", d.college_code], ["Centre", d.centre_name],
            ["Centre Code", d.centre_code]
        ].forEach(x => {
            let r = e("tr");
            r.append(e("th", "", x[0]));
            r.append(e("td", "", v(x[1])));
            t.append(r);
        });

        s.append(t);
        c.append(s);
        // Semester
        for (let n = 1; n <= 4; n++) {
            let p = "s" + n + "_"
                , s = e("div", "semester-container")
                , z = e("div", "semester-summary");

            s.append(e("h3", "semester-title", "Semester " + n));
            [
                ["Total", d[p + "total"]],
                ["Percentage", d[p + "percentage"]],
                ["SGPA", d[p + "sgpa"]],
                ["Grade", d[p + "grade"]],
                ["Result", d[p + "result"]]
            ].forEach(x => {
                let b = e("div", "summary-box");
                b.append(e("span", "summary-label", x[0]));
                b.append(e("strong", "summary-value", v(x[1])));
                z.append(b);
            });

            s.append(z);

            let t = e("table", "result-table paper-table"), h = e("tr"), thead = e("thead"), b = e("tbody");
            ["Paper", "Code", "Paper Name", "Internal", "Theory", "Total", "Grade"].forEach(x => h.append(e("th", "", x)));

            thead.append(h);
            t.append(thead);
            for (let i = 1; i <= 4; i++) {
                let r = e("tr");

                [
                    "Paper " + i,
                    d[p + "paper" + i + "c"],
                    d[p + "papername" + i],
                    d[p + "pap" + i + "int"],
                    d[p + "pap" + i + "th"],
                    d[p + "pap" + i + "tot"],
                    d[p + "pap" + i + "_grade"]
                ].forEach(x => r.append(e("td", "", v(x))));

                b.append(r);
            }

            t.append(b);
            s.append(t);
            c.append(s);
        }

        // Final Result
        let f = e("div", "final-result");
        f.append(e("h3", "section-title", "Final Result"));

        let t2 = e("table", "result-table");

        [
            ["Total Marks", d.f_total],
            ["Percentage", v(d.f_percentage) + "%"],
            ["Grade", d.f_grade],
            ["CGPA", d.f_cgpa],
            ["Division", d.f_division],
            ["Result", d.result_status],
            ["Marksheet No.", d.marksheetno],
            ["Exam", d.examid],
            ["Held", d.held_month + " " + d.held_year],
            ["Publication", d.date_publication],
            ["Remarks", d.f_remarks]
        ].forEach(x => {
            let r = e("tr");
            r.append(e("th", "", x[0]));
            r.append(e("td", "", v(x[1])));
            t2.append(r);
        });

        f.append(t2);
        c.append(f);

        var g = e("div", "button-group")
            , b = e("button", "back-button", "Back")
            , p = e("button", "print-button", "Print Result");

        g.append(b, p);
        c.append(g);
        p.onclick = () => window.print();
        b.onclick = bc;


    }
    , vi = function (a, b) {
        let u = new URL(location);
        u.search = '';
        u.searchParams.set(a, b);
        location.href = u.toString();
    }
    , th = `<thead><tr><th>No.</th><th>Roll No.</th><th>Name</th><th>College</th><th>Marks</th><th>Percentage</th><th>Action</th></tr></thead>`
    , lf = (d) => {
        document.body.innerHTML = "";
        let h = e("h2", "", `Result : NPU All Master of Arts (${d[0].subject}) [ 2023-2025 ]`);
        let t = e("table"), b = e("tbody");

        document.title = h.textContent;
        t.innerHTML = th;
        t.append(b);
        d.sort((a, b) => b.f_percentage - a.f_percentage);
        let n = 0;



        d.forEach(x => {
            if (x.sassion != "2023-2025") return;

            let r = e("tr");
            r.className = (x.f_division || "").replace(" ", "-").toLowerCase();

            [
                ++n,
                x.ansidrno,
                x.sname,
                x.college_name,
                x.f_total,
                x.f_percentage
            ].forEach(x => r.append(e("th", "", x)));

            let td = e("td"), btn = e("button", "", "View");
            btn.onclick = () => vi("rollno", x.rollno);
            td.append(btn);
            r.append(td);
            b.append(r);
        });

        const r = e("button", "back-button", "Back");
        r.onclick = bc;

        document.body.append(h, t, r);
    }
    , hm = (data) => {

        // DOM Elements Creation
        const root = e("div", "__root");
        let mainTitle = e("h2", "main-title", "🎓 NPU All Master of Arts - Merit List");

        let section = e("section", "topper-section");
        let sectionTitle = e("h3", "section-title", "🏆 Top Achievers & Subject Ranks");
        let listsContainer = e("div", "lists-container");

        section.append(sectionTitle, listsContainer);

        for (const [k, j] of Object.entries(data)) {
            let listItem = e("div", "list-item");
            let itemRow = e("div", "item-row");

            let contentArea = e("div", "content-area");

            // Name ke baad Roll Number (agar j.roll_no available ho toh wo, warna key 'k')
            let nameContainer = e("div", "name");
            nameContainer.innerHTML = `${j.sname} <span class="roll-no">[ ${j.rollno} ]</span>`;

            contentArea.append(
                nameContainer,
                e("div", "collage", `🏛️ ${j.college_name}`)
            );

            // Subject aur Rank ko right side paas-paas dikhane ke liye
            let rightInfo = e("div", "right-info");
            let subTag = e("span", "sub-tag", `Subject: ${k}`);
            let rankBadge = e("div", "rank", `Rank #${j.f_percentage}`);
            rightInfo.append(subTag, rankBadge);

            itemRow.append(contentArea, rightInfo);

            // Button inside the list item footer
            let itemFooter = e("div", "item-footer");
            let viewBtn = e("button", "view-btn", "View All Rank / Details");

            viewBtn.onclick = () => vi("sub", k);

            itemFooter.append(viewBtn);
            listItem.append(itemRow, itemFooter);
            listsContainer.append(listItem);
        }



        root.append(mainTitle, section);
        document.body.append(root);
    }
    , s = new URLSearchParams(window.location.search).get("rollno");


// Class ka object banayein
const api = new StudentAPI(location.origin);

// 1. Naya Student Insert karne ke liye:
async function addStudent() {
    const student = {
        slno: 1003245,
        rollno: "240011900780",
        sname: "CHANDAN SINGH",
        subject: "Botany",
        s3_percentage: "69"
    };
    const result = await api.createStudent(student);
    console.log("Inserted:", result);
}

// 2. Sabhi Subjects ke Toppers dekhne ke liye:
async function showToppers() {
    const toppers = await api.getAllSubjectToppers();

    console.log(subject_roll_numbers);

    hm(toppers)

    console.log("All Toppers:", toppers);
}

// 3. Roll Number se Student dhoondhne ke liye:
async function findStudent(rollno) {
    const student = await api.getStudentByRollNo(rollno);
    rp(student);
    console.log("Found Student:", student);
}

// 4. Sabhi Subjects ki List mangwane ke liye:
async function loadSubjects(sub) {
    // const subjects = await api.getAllSubjects();
    const subjects = await api.getStudentsBySubject(sub);
    lf(subjects)
    console.log("Subjects:", subjects);
}


const get_key = e => new URLSearchParams(window.location.search).get(e)
const sub = get_key("sub")
const rollno = get_key("rollno")


if (sub) {
    loadSubjects(sub)
}
else if (rollno) {
    findStudent(rollno)
}
else {
    showToppers()
}
