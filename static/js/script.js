!(function () {
    class URLState {
        constructor(a = true, u = location.href) {
            this.a = a; this.e = true; this.c = new Set; this.u = new URL(u);
            ['popstate', 'hashchange'].forEach(e => window.addEventListener(e, () => this.navigate(location.href)));
            this.check();
        }
        onChange(f) { typeof f == 'function' && this.c.add(f); return this; }
        check() {
            let o = this.o; this.p = new URLSearchParams(this.u.search); this.o = this.u.href;
            Object.assign(this, Object.fromEntries(['href', 'host', 'hostname', 'origin', 'pathname', 'port', 'search', 'protocol'].map(k => [k, this.u[k]])));
            this.e && o != this.o && this.change(); return this;
        }
        change() { this.c.forEach(f => f.call(this, this.u)); }
        push(x = true) { this.a && history.pushState({ u: this.href }, '', this.u); x && this.check(); return this; }
        navigate(u, x = true) { this.u = new URL(u, location.origin); this.p = new URLSearchParams(this.u.search); return this.push(x); }
        get(k) { return this.p.get(k); }
        set(k, v, x = true) { this.p.set(k, v); this.u.search = this.p; return this.push(x); }
        delete(k, x = true) { this.p.delete(k); this.u.search = this.p; return this.push(x); }
        clear(x) { this.p = new URLSearchParams; this.u.search = ''; return x && this.push(x); }
        back() { return history.back(); }
        reload() { return this.a && location.reload(); }
    }

    class StudentAPI {
        constructor(b = location.origin) { this.b = b; }
        async _(e, o = {}) {
            let r = await fetch(this.b + e, o);
            if (!r.ok) throw new Error(((await r.json()).detail) || `HTTP ${r.status}`);
            return r.json();
        }
        cs(d) { return this._("/results/", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(d) }); }
        getAllStudents(s = 0, l = 10) { return this._(`/results/?skip=${s}&limit=${l}`); }
        grsn(s) { return this._(`/results/${s}`); }
        gsbr(r) { return this._(`/results/rollno/${r}`); }
        gstl() { return this._("/toppers"); }
        getTopperBySubject(s) { return this._(`/toppers/subject/${encodeURIComponent(s)}`); }
        gsbs(s, k = 0, l = 5000) { return this._(`/students/subject/${encodeURIComponent(s)}?skip=${k}&limit=${l}`); }
        gasa() { return this._("/subjects/"); }
    }

    const r = new URLState(),
        api = new StudentAPI(),
        bc = () => r.back(),
        vi = (a, b) => { r.clear(); r.set(a, b); },
        e = (t, c, x) => {
            let d = document.createElement(t);
            if (c) d.className = c;
            if (Array.isArray(x)) d.append(...x);
            else if (x != null) typeof x == "string" && x.includes("<") ? d.innerHTML = x : d.textContent = x;
            return d;
        },
        v = x => x == null || x === "" ? "-" : String(x).trim(),
        makeTbl = (rows, cls = "N08") => {
            let t = e("table", cls);
            rows.forEach(x => t.append(e("tr", "", [e("th", "", x[0]), e("td", "", v(x[1]))])));
            return t;
        },
        rp = d => {
            if (!d) return confirm("Student Not Found") && bc();
            let c = e("div", "", [
                e("h2", "N02", "Student Result Details"),
                e("div", "N03", [
                    e("h3", "N06", "Student Details"),
                    makeTbl([
                        ["Name", d.sname], ["Father", d.fname], ["Mother", d.mname], ["DOB", d.dob], ["Gender", d.gender],
                        ["Category", d.category], ["Reg. No.", d.regno], ["Roll No.", d.rollno], ["Admit ID", d.admitid],
                        ["Candidate", d.candidate_type], ["Class Roll", d.clrollno], ["Course", d.coursename], ["Stream", d.stream],
                        ["Subject", d.subject], ["Honours", d.honours], ["Session", d.sassion], ["College", d.college_name],
                        ["College Code", d.college_code], ["Centre", d.centre_name], ["Centre Code", d.centre_code]
                    ])
                ])
            ]);

            for (let n = 1; n <= 4; n++) {
                let p = "s" + n + "_",
                    z = e("div", "N10", ["Total", "Percentage", "SGPA", "Grade", "Result"].map(k =>
                        e("div", "N11", [e("span", "N12", k), e("strong", "N13", v(d[p + k.toLowerCase()]))])
                    )),
                    tb = e("tbody");

                for (let i = 1; i <= 4; i++) {
                    tb.append(e("tr", "", ["Paper " + i, d[p + "paper" + i + "c"], d[p + "papername" + i], d[p + "pap" + i + "int"], d[p + "pap" + i + "th"], d[p + "pap" + i + "tot"], d[p + "pap" + i + "_grade"]].map(x => e("td", "", v(x)))));
                }

                let paperTbl = e("table", "N08 N09", [
                    e("thead", "", [e("tr", "", ["Paper", "Code", "Paper Name", "Internal", "Theory", "Total", "Grade"].map(x => e("th", "", x)))]),
                    tb
                ]);

                c.append(e("div", "N04", [e("h3", "N07", "Semester " + n), z, paperTbl]));
            }

            let btnBack = e("button", "N90", "Back"),
                btnPrint = e("button", "N90", "Print Result");
            btnBack.onclick = bc; btnPrint.onclick = () => window.print();

            c.append(
                e("div", "N05", [
                    e("h3", "N06", "Final Result"),
                    makeTbl([
                        ["Total Marks", d.f_total], ["Percentage", v(d.f_percentage) + "%"], ["Grade", d.f_grade],
                        ["CGPA", d.f_cgpa], ["Division", d.f_division], ["Result", d.result_status],
                        ["Marksheet No.", d.marksheetno], ["Exam", d.examid], ["Held", d.held_month + " " + d.held_year],
                        ["Publication", d.date_publication], ["Remarks", d.f_remarks]
                    ])
                ]),
                e("div", "N14", [btnBack, btnPrint])
            );
            return c;
        },
        lf = d => {
            document.title = `Result : NPU All Master of Arts (${d[0]?.subject}) [ 2023-2025 ]`;
            let b = e("tbody"), n = 0;
            d.sort((a, b) => b.f_percentage - a.f_percentage).forEach(x => {
                if (x.sassion != "2023-2025") return;
                let btn = e("button", "", "View");
                btn.onclick = () => vi("rollno", x.rollno);
                let tr = e("tr", (x.f_division || "").replace(" ", "-").toLowerCase(), [
                    ...[++n, x.ansidrno, x.sname, x.college_name, x.f_total, x.f_percentage].map(v => e("th", "", v)),
                    e("td", "", [btn])
                ]);
                b.append(tr);
            });

            let btnBack = e("button", "N90", "Back");
            btnBack.onclick = bc;
            return e("main", null, [
                e("h2", "N02", document.title),
                e("table", "", [e("thead", "", [e("tr", "", ["No.", "Roll No.", "Name", "College", "Marks", "Percentage", "Action"].map(x => e("th", "", x)))]), b]),
                btnBack
            ]);
        },
        hm = a => {
            let b = e("div", "N91");
            for (let [k, f] of Object.entries(a)) {
                let btn = e("button", "N99", "View All Rank / Details");
                btn.onclick = () => vi("sub", k);
                b.append(e("div", "N92", [
                    e("div", "N93", [
                        e("div", "N94", [
                            e("div", "name", `${f.sname} <span class="N95">[ ${f.rollno} ]</span>`),
                            e("div", "collage", `🏛️ ${f.college_name}`)
                        ]),
                        e("div", "N96", [e("span", "N97", `${k}`), e("div", "rank", `${f.f_percentage} %`)])
                    ]),
                    e("div", "N98", [btn])
                ]));
            }
            return e("div", "__root", [e("h2", "N02", "🎓 NPU All Master of Arts - Merit List"), e("section", "topper-section", [e("h3", "N06", "🏆 Top Achievers & Subject Ranks"), b])]);
        };

    r.onChange(async u => {
        let s = u.searchParams.get("sub"), n = u.searchParams.get("rollno");
        document.body.replaceChildren(s ? lf(await api.gsbs(s)) : n ? rp(await api.gsbr(n)) : hm(await api.gstl()));
    });
    r.change();
}())
