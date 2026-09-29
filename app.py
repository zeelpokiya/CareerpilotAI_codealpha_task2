import os
import streamlit as st
import pandas as pd

from agent.graph import create_careerpilot_graph
from utils.report_generator import generate_career_report


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareerPilot AI | Intelligent Career & Skill Roadmap Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# LOAD EXTERNAL CSS FILE
# ============================================================

def load_css(file_path="assets/style.css"):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Career Analysis"

if "result" not in st.session_state:
    st.session_state.result = None

if "profile" not in st.session_state:
    st.session_state.profile = {}

if "coach_messages" not in st.session_state:
    st.session_state.coach_messages = []


# ============================================================
# HELPER FUNCTIONS & SPEED OPTIMIZATION (CACHE)
# ============================================================

def list_value(value):
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [x.strip() for x in value.split(",") if x.strip()]
    return []


@st.cache_resource
def get_cached_graph():
    return create_careerpilot_graph()


def run_analysis(profile):
    graph = get_cached_graph()
    state = {
        "name": profile["name"],
        "education": profile["education"],
        "experience": profile["experience"],
        "skills": profile["skills"],
        "interests": profile["interests"],
        "target_role": profile["target_role"],
    }
    return graph.invoke(state)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="padding: 12px 4px 24px 4px; border-bottom: 1px solid #1E293B; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="background: #2563EB; width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px;">🚀</div>
                <div>
                    <h2 style="margin: 0; font-size: 18px; font-weight: 800; color: #FFFFFF !important; letter-spacing: -0.3px;">CareerPilot AI</h2>
                    <p style="margin: 0; font-size: 11px; color: #64748B !important; font-weight: 500;">Next-Gen Career Intelligence</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    pages = [
        ("🎯", "Career Analysis"),
        ("🏠", "Dashboard"),
        ("📊", "Skill Gap"),
        ("🗺️", "Roadmap"),
        ("💡", "Projects"),
        ("📄", "Report"),
        ("🤖", "AI Coach"),
        ("ℹ️", "About"),
    ]

    for icon, page_name in pages:
        if st.button(
            f"{icon}   {page_name}",
            key=f"sidebar_{page_name}",
            use_container_width=True,
        ):
            st.session_state.page = page_name
            st.rerun()


# ============================================================
# PAGE 1: CAREER ANALYSIS (PERFECTLY ALIGNED BOTH COLUMNS)
# ============================================================
# ============================================================
# PAGE 1: CAREER ANALYSIS
# ============================================================

if st.session_state.page == "Career Analysis":

  # HEADER CONTAINER
    st.markdown(
        """
        <div class="saas-card" style="margin-bottom: 24px; padding: 20px 24px; border-left: 5px solid #2563EB;">
            <h1 style="font-size: 26px; font-weight: 800; color: #0F172A !important; letter-spacing: -0.5px; margin-bottom: 6px;">
                🎯 Career Analysis & Profile Setup
            </h1>
            <p style="color: #64748B !important; font-size: 14px; margin: 0; font-weight: 500;">
                Fill in your details below to generate an AI-powered career roadmap and skill gap evaluation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col_left, col_right = st.columns([1.1, 0.9], gap="large")

    # LEFT COLUMN: Personal Details Container
    with col_left:
        # main card start
        st.markdown('<div class="saas-card" style="padding: 0px 0px 20px 0px; overflow: hidden;">', unsafe_allow_html=True)
        
        # Header inside the card box
        st.markdown(
            """
            <div class="summary-header" style="border-radius: 12px 12px 0 0; margin-bottom: 20px;">
                <span style="font-size: 20px;">👤</span>
                <span>Personal Details & Competencies</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div style="padding: 0 20px;">', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input(
                "Full Name",
                value="",
                placeholder="e.g. Rahul Patel",
                key="profile_name"
            )
        with c2:
            experience = st.selectbox(
                "Experience Level",
                ["Select Experience Level", "Fresher", "Internship", "1 Year Experience", "2+ Years Experience"],
                key="profile_experience",
            )

        education = st.text_input(
            "Education / Qualification",
            value="",
            placeholder="e.g. BCA, B.Tech CS, Diploma in IT",
            key="profile_education"
        )

        skills_text = st.text_input(
            "Your Current Skills (comma separated)",
            value="",
            placeholder="e.g. Python, SQL, Java, HTML",
            key="profile_skills"
        )

        interests_text = st.text_input(
            "Your Interests (comma separated)",
            value="",
            placeholder="e.g. Data Science, Web Development",
            key="profile_interests"
        )

        target_role = st.text_input(
            "Target Role / Preferred Career",
            value="",
            placeholder="e.g. Data Scientist, Full Stack Developer",
            key="profile_target"
        )
        
        st.markdown('</div>', unsafe_allow_html=True) # inner padding end
        st.markdown('</div>', unsafe_allow_html=True) # main card end

    # RIGHT COLUMN: Live Profile Summary Container
    with col_right:
        # main card start
        st.markdown('<div class="saas-card" style="padding: 0px 0px 20px 0px; overflow: hidden; height: 100%;">', unsafe_allow_html=True)
        
        # Header inside the card box
        st.markdown(
            """
            <div class="summary-header" style="border-radius: 12px 12px 0 0; margin-bottom: 20px;">
                <span style="font-size: 20px;">👁️</span>
                <span>Live Profile Summary</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div style="padding: 0 20px;">', unsafe_allow_html=True)

        s1, s2 = st.columns(2)
        with s1:
            st.markdown("<p style='font-size:12px; font-weight:700; color:#64748B !important; margin:0;'>CANDIDATE NAME</p>", unsafe_allow_html=True)
            if name.strip():
                st.markdown(f"<div class='profile-value-active'>{name.strip()}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='profile-value-empty'>Waiting for input...</div>", unsafe_allow_html=True)

            st.write("")

            st.markdown("<p style='font-size:12px; font-weight:700; color:#64748B !important; margin:0;'>QUALIFICATION</p>", unsafe_allow_html=True)
            if education.strip():
                st.markdown(f"<div class='profile-value-active'>{education.strip()}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='profile-value-empty'>Waiting for input...</div>", unsafe_allow_html=True)

        with s2:
            st.markdown("<p style='font-size:12px; font-weight:700; color:#64748B !important; margin:0;'>EXPERIENCE LEVEL</p>", unsafe_allow_html=True)
            if experience != "Select Experience Level":
                st.markdown(f"<div class='profile-value-active'>{experience}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='profile-value-empty'>Not selected</div>", unsafe_allow_html=True)

            st.write("")

            st.markdown("<p style='font-size:12px; font-weight:700; color:#64748B !important; margin:0;'>TARGET ROLE</p>", unsafe_allow_html=True)
            if target_role.strip():
                st.markdown(f"<div class='profile-value-active' style='color:#2563EB !important;'>{target_role.strip()}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='profile-value-empty'>Waiting for input...</div>", unsafe_allow_html=True)

        st.divider()

        st.markdown("<p style='font-size: 12px; font-weight: 700; color: #475569 !important; margin-bottom: 6px;'>CURRENT SKILLS TAGS</p>", unsafe_allow_html=True)
        skills_list = [s.strip() for s in skills_text.split(",") if s.strip()]
        pills_html = "".join([f'<span class="badge-pill">{s}</span>' for s in skills_list])
        st.markdown(pills_html if pills_html else "<span class='profile-value-empty'>Type skills above to see tags</span>", unsafe_allow_html=True)

        st.write("")

        st.markdown("<p style='font-size: 12px; font-weight: 700; color: #475569 !important; margin-bottom: 6px;'>KEY INTERESTS TAGS</p>", unsafe_allow_html=True)
        interests_list = [i.strip() for i in interests_text.split(",") if i.strip()]
        pills_purple_html = "".join([f'<span class="badge-pill badge-pill-purple">{i}</span>' for i in interests_list])
        st.markdown(pills_purple_html if pills_purple_html else "<span class='profile-value-empty'>Type interests above to see tags</span>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True) # inner padding end
        st.markdown('</div>', unsafe_allow_html=True) # main card end

    # Submit Button
    st.markdown("<br>", unsafe_allow_html=True)
    analyze = st.button("🚀 Analyze My Career Path", type="primary", use_container_width=True)

    # PROCESS CARDS SECTION
    st.markdown('<div class="saas-card" style="margin-top: 24px;">', unsafe_allow_html=True)
    st.markdown('<div class="saas-card-header">⚡ How CareerPilot Processing Engine Works</div>', unsafe_allow_html=True)

    p1, p2, p3, p4, p5 = st.columns(5, gap="medium")

    steps = [
        ("01", "Profile Audit", "Deep-scans your background, experience level, and qualifications."),
        ("02", "Match Engine", "Calculates percentage fit against high-demand career tracks."),
        ("03", "Gap Assessment", "Pinpoints missing technical & soft skills for your target role."),
        ("04", "Roadmap Creator", "Generates milestone-based learning & step-by-step guidance."),
        ("05", "Interactive Coach", "Provides portfolio project ideas & real-time career advice.")
    ]

    cols = [p1, p2, p3, p4, p5]
    for idx, (num, title, desc) in enumerate(steps):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="pro-process-card">
                    <div>
                        <div class="pro-step-badge">{num}</div>
                        <div class="pro-step-title">{title}</div>
                        <div class="pro-step-desc">{desc}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)

    # Form Submission Logic
    if analyze:
        skills = [x.strip() for x in skills_text.split(",") if x.strip()]
        interests = [x.strip() for x in interests_text.split(",") if x.strip()]

        if not name.strip():
            st.warning("⚠️ Please enter your Full Name.")
        elif experience == "Select Experience Level":
            st.warning("⚠️ Please select your Experience Level.")
        elif not education.strip():
            st.warning("⚠️ Please enter your Education/Qualification.")
        elif not skills:
            st.warning("⚠️ Please enter at least one skill.")
        elif not target_role.strip():
            st.warning("⚠️ Please enter your Target Role.")
        else:
            profile = {
                "name": name.strip(),
                "education": education.strip(),
                "experience": experience,
                "target_role": target_role.strip(),
                "skills": skills,
                "interests": interests,
            }

            st.session_state.profile = profile

            with st.spinner("Analyzing profile and generating career insights..."):
                try:
                    result = run_analysis(profile)
                    st.session_state.result = result
                    st.session_state.page = "Dashboard"
                    st.rerun()
                except Exception as error:
                    st.error("Career analysis failed.")
                    st.exception(error)


# ============================================================
# PAGE 2: DASHBOARD
# ============================================================

elif st.session_state.page == "Dashboard":
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="font-size: 26px; font-weight: 800; color: #0F172A !important; letter-spacing: -0.5px; margin-bottom: 4px;">🏠 Career Intelligence Overview</h1>
            <p style="color: #64748B !important; font-size: 14px; margin: 0;">Your personalized career intelligence, skill insights, and next-step recommendations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    result = st.session_state.result
    if not result:
        st.info("⚠️ Please complete Career Analysis first to view your personal dashboard.")
    else:
        readiness = result.get("readiness", {})
        recommendations = result.get("career_recommendations", [])
        gaps = list_value(result.get("skill_gaps", []))
        projects = result.get("project_recommendations", [])

        # TOP METRIC CARDS
        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown(
                f"""
                <div class="metric-card" style="border-left: 4px solid #2563EB;">
                    <div class="metric-label">📊 Readiness Score</div>
                    <div class="metric-value-primary">{readiness.get('overall', 0)}%</div>
                    <span style="font-size: 11px; color: #64748B !important;">Based on skill qualification</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with m2:
            top_career = recommendations[0].get("career", "N/A") if recommendations else "N/A"
            st.markdown(
                f"""
                <div class="metric-card" style="border-left: 4px solid #10B981;">
                    <div class="metric-label">🎯 Top Matched Role</div>
                    <div class="metric-value-dark">{top_career}</div>
                    <span style="font-size: 11px; color: #64748B !important;">Highest compatibility fit</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with m3:
            st.markdown(
                f"""
                <div class="metric-card" style="border-left: 4px solid #F59E0B;">
                    <div class="metric-label">📌 Identified Skill Gaps</div>
                    <div class="metric-value-primary" style="color: #D97706 !important;">{len(gaps)} Key Skills</div>
                    <span style="font-size: 11px; color: #64748B !important;">Targeted for improvement</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with m4:
            st.markdown(
                f"""
                <div class="metric-card" style="border-left: 4px solid #8B5CF6;">
                    <div class="metric-label">💡 Portfolio Projects</div>
                    <div class="metric-value-primary" style="color: #7C3AED !important;">{len(projects)} Suggested</div>
                    <span style="font-size: 11px; color: #64748B !important;">To boost profile strength</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # CAREER RECOMMENDATIONS CARDS
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.markdown('<div class="saas-card-header">🚀 AI-Recommended Career Paths</div>', unsafe_allow_html=True)

        if recommendations:
            for index, item in enumerate(recommendations, start=1):
                career_title = item.get("career", "Career Track")
                match_score = item.get("score", 0)
                desc = item.get("description", "No description provided.")

                st.markdown(
                    f"""
                    <div class="career-recommend-card">
                        <div style="flex: 1; padding-right: 20px;">
                            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                                <span style="background: #0F172A; color: #FFFFFF !important; font-size: 12px; font-weight: 800; border-radius: 6px; width: 24px; height: 24px; display: inline-flex; align-items: center; justify-content: center;">{index}</span>
                                <h3 style="margin: 0; font-size: 18px; font-weight: 800; color: #0F172A !important;">{career_title}</h3>
                            </div>
                            <p style="margin: 0; font-size: 14px; color: #475569 !important; line-height: 1.5;">{desc}</p>
                        </div>
                        <div>
                            <div class="match-score-badge">{match_score}% Match</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("No recommendations generated.")

        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# PAGE 3: SKILL GAP
# ============================================================

elif st.session_state.page == "Skill Gap":
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="font-size: 26px; font-weight: 800; color: #0F172A !important;">📊 Skill Gap Analysis</h1>
            <p style="color: #64748B !important; font-size: 14px; margin: 0;">Detailed breakdown of existing abilities versus required competencies.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    result = st.session_state.result
    if not result:
        st.info("Please complete Career Analysis first.")
    else:
        current_skills = list_value(result.get("skills", []))
        gaps = list_value(result.get("skill_gaps", []))
        
        left, right = st.columns(2, gap="large")
        with left:
            st.markdown('<div class="saas-card">', unsafe_allow_html=True)
            st.markdown('<div class="saas-card-header">✅ Existing Skills</div>', unsafe_allow_html=True)
            pills_html = "".join([f'<span class="badge-pill">{s}</span>' for s in current_skills])
            st.markdown(pills_html if pills_html else "No skills recorded.", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right:
            st.markdown('<div class="saas-card">', unsafe_allow_html=True)
            st.markdown('<div class="saas-card-header">📌 Targeted Skill Gaps</div>', unsafe_allow_html=True)
            pills_purple = "".join([f'<span class="badge-pill badge-pill-purple">{g}</span>' for g in gaps])
            st.markdown(pills_purple if pills_purple else "No critical skill gaps identified!", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# PAGE 4: ROADMAP
# ============================================================

elif st.session_state.page == "Roadmap":
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="font-size: 26px; font-weight: 800; color: #0F172A !important; letter-spacing: -0.5px;">🗺️ Structured Learning Roadmap</h1>
            <p style="color: #64748B !important; font-size: 14px; margin: 0;">Step-by-step career path meticulously mapped to achieve your target role.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    result = st.session_state.result
    if not result:
        st.info("⚠️ Please complete Career Analysis first to view your learning roadmap.")
    else:
        roadmap = result.get("roadmap", [])
        if roadmap:
            for idx, phase in enumerate(roadmap, start=1):
                phase_name = phase.get('phase', f'Phase {idx}')
                phase_title = phase.get('title', 'Skill Mastery')
                duration = phase.get('duration', 'Flexible')
                topics = phase.get('topics', [])

                st.markdown(
                    f"""
                    <div class="roadmap-card">
                        <div class="roadmap-header">
                            <div class="roadmap-phase-title">
                                <span style="background: #2563EB; color: white; border-radius: 8px; width: 32px; height: 32px; display: inline-flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800;">{idx}</span>
                                <span>{phase_name} — {phase_title}</span>
                            </div>
                            <div class="roadmap-badge">
                                ⏱️ {duration}
                            </div>
                        </div>
                    """,
                    unsafe_allow_html=True
                )

                for topic in topics:
                    st.markdown(
                        f"""
                        <div class="roadmap-topic-item">
                            <span style="color: #2563EB;">⚡</span>
                            <span>{topic}</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("No roadmap generated.")


# ============================================================
# PAGE 5: PROJECTS
# ============================================================

elif st.session_state.page == "Projects":
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="font-size: 26px; font-weight: 800; color: #0F172A !important;">💡 Recommended Portfolio Projects</h1>
            <p style="color: #64748B !important; font-size: 14px; margin: 0;">Build these projects to showcase relevant skills to hiring managers.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    result = st.session_state.result
    if not result:
        st.info("Please complete Career Analysis first.")
    else:
        projects = result.get("project_recommendations", [])
        for index, project in enumerate(projects, start=1):
            st.markdown('<div class="saas-card">', unsafe_allow_html=True)
            st.markdown(f"### {index}. {project.get('title', 'Project')}")
            st.caption(f"Difficulty Level: {project.get('difficulty', 'Intermediate')}")
            if project.get("description"):
                st.write(project["description"])
            st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# PAGE 6: REPORT
# ============================================================

elif st.session_state.page == "Report":
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="font-size: 26px; font-weight: 800; color: #0F172A !important;">📄 Detailed Career Report</h1>
            <p style="color: #64748B !important; font-size: 14px; margin: 0;">Download or read your generated Markdown analysis report.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    result = st.session_state.result
    if not result:
        st.info("Please complete Career Analysis first.")
    else:
        report = generate_career_report(result)
        st.download_button(
            "⬇️ Download Markdown Report",
            data=report,
            file_name="CareerPilot_AI_Report.md",
            mime="text/markdown",
            use_container_width=True,
        )
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        st.markdown(report)
        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# PAGE 7: AI COACH
# ============================================================

elif st.session_state.page == "AI Coach":
    st.markdown(
        """
        <div style="margin-bottom: 24px;">
            <h1 style="font-size: 26px; font-weight: 800; color: #0F172A !important;">🤖 AI Career Coach</h1>
            <p style="color: #64748B !important; font-size: 14px; margin: 0;">Interactive assistant to answer career, interview, or skill guidance questions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if not st.session_state.result:
        st.info("Please complete Career Analysis first.")
    else:
        for message in st.session_state.coach_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        question = st.chat_input("Ask your AI Career Coach...")
        if question:
            st.session_state.coach_messages.append({"role": "user", "content": question})
            profile = st.session_state.profile
            prompt = f"User Question: {question}\nProfile Context: {profile}"
            try:
                from ollama import chat
                response = chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
                answer = response["message"]["content"]
            except Exception as error:
                answer = f"Ollama connection failed.\n\nError details: {error}"

            st.session_state.coach_messages.append({"role": "assistant", "content": answer})
            st.rerun()


# ============================================================
# PAGE 8: ABOUT
# ============================================================

elif st.session_state.page == "About":
    st.markdown(
        """
        <div class="about-hero">
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 12px;">
                <div style="background: #2563EB; width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 26px;">🚀</div>
                <div>
                    <h1 style="margin: 0; font-size: 28px; font-weight: 800; color: #FFFFFF !important;">CareerPilot AI</h1>
                    <p style="margin: 0; color: #94A3B8 !important; font-size: 14px;">Autonomous Career Intelligence & Skill Gap Navigation Engine</p>
                </div>
            </div>
            <p style="color: #CBD5E1 !important; font-size: 15px; line-height: 1.6; margin: 17px 0 0 0;">
                CareerPilot AI is designed to bridge the gap between human ambition and market demands. Powered by advanced AI agents and graph architectures, it analyzes your competencies, identifies high-impact skill gaps, and constructs realistic, actionable career pathways.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h3 style='font-size: 18px; font-weight: 800; color: #0F172A !important; margin-bottom: 16px;'>✨ Core Architectural Features</h3>", unsafe_allow_html=True)

    a1, a2, a3 = st.columns(3)

    with a1:
        st.markdown(
            """
            <div class="about-feature-box">
             <div style="font-size: 30px; margin-bottom: 10px;color: #0F172A">🧠Agentic Intelligence</div>
                <h4 style="margin: 0 0 8px 0; font-size: 16px; font-weight: 800; color: #0F172A !important;"></h4>
                <p style="margin: 0; font-size: 13px; color: #64748B !important; line-height: 1.5;">Uses stateful LangGraph workflows to perform deep skill-matching and structured reasoning.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a2:
        st.markdown(
            """
            <div class="about-feature-box">
                <div style="font-size: 28px; margin-bottom: 10px;">📊 Targeted Gap Analysis</div>
                <h4 style="margin: 0 0 8px 0; font-size: 16px; font-weight: 800; color: #0F172A !important;"></h4>
                <p style="margin: 0; font-size: 15px; color: #64748B !important; line-height: 1.5;">Evaluates current knowledge against real job requirements to pinpoint exact learning targets.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with a3:
        st.markdown(
            """
            <div class="about-feature-box">
                <div style="font-size: 28px; margin-bottom: 10px;">🗺️ Dynamic Roadmaps</div>
                <h4 style="margin: 0 0 8px 0; font-size: 16px; font-weight: 800; color: #0F172A !important;"></h4>
                <p style="margin: 0; font-size: 13px; color: #64748B !important; line-height: 1.5;">Generates phase-wise duration estimates and curated project recommendations for portfolio building.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()
st.caption("CareerPilot AI  ·  Intelligent Career & Skill Roadmap Assistant")