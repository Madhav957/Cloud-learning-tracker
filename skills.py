from flask import Blueprint, request, jsonify
from db import db

bp = Blueprint("skills", __name__)


# Create study session
@bp.route("/study-sessions", methods=["POST"])
def create_study_session():

    data = request.get_json()

    session_date = data["session_date"]
    duration_minutes = data["duration_minutes"]
    topic = data["topic"]
    learning_outcome = data["learning_outcome"]
    courseid = data["courseid"]
    userid = data["userid"]

    cursor = db.cursor()

    query = """
    INSERT INTO study_sessions (
        session_date,
        duration_minutes,
        topic,
        learning_outcome,
        courseid,
        userid
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            session_date,
            duration_minutes,
            topic,
            learning_outcome,
            courseid,
            userid
        )
    )

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Study session created!"
    }), 201


# Get all study sessions of a user
@bp.route("/users/<userid>/study-sessions", methods=["GET"])
def get_study_sessions(userid):

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM study_sessions
    WHERE userid = %s
    """

    cursor.execute(query, (userid,))

    sessions = cursor.fetchall()

    cursor.close()

    return jsonify(sessions)


# Get one study session
@bp.route("/study-sessions/<sessionid>", methods=["GET"])
def get_study_session(sessionid):

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM study_sessions
    WHERE sessionid = %s
    """

    cursor.execute(query, (sessionid,))

    session = cursor.fetchone()

    cursor.close()

    return jsonify(session)


# Update study session
@bp.route("/study-sessions/<sessionid>", methods=["PUT"])
def update_study_session(sessionid):

    data = request.get_json()

    session_date = data["session_date"]
    duration_minutes = data["duration_minutes"]
    topic = data["topic"]
    learning_outcome = data["learning_outcome"]
    courseid = data["courseid"]

    cursor = db.cursor()

    query = """
    UPDATE study_sessions
    SET session_date = %s,
        duration_minutes = %s,
        topic = %s,
        learning_outcome = %s,
        courseid = %s
    WHERE sessionid = %s
    """

    cursor.execute(
        query,
        (
            session_date,
            duration_minutes,
            topic,
            learning_outcome,
            courseid,
            sessionid
        )
    )

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Study session updated!"
    })


# Delete study session
@bp.route("/study-sessions/<sessionid>", methods=["DELETE"])
def delete_study_session(sessionid):

    cursor = db.cursor()

    query = """
    DELETE FROM study_sessions
    WHERE sessionid = %s
    """

    cursor.execute(query, (sessionid,))

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Study session deleted!"
    })


# =========================================================
# SKILLS
# =========================================================

# Create skill
@bp.route("/skills", methods=["POST"])
def create_skill():

    data = request.get_json()

    skill_name = data["skill_name"]
    proficiency = data["proficiency"]
    category = data["category"]
    userid = data["userid"]

    cursor = db.cursor()

    query = """
    INSERT INTO skills (
        skill_name,
        proficiency,
        category,
        userid
    )
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            skill_name,
            proficiency,
            category,
            userid
        )
    )

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Skill created!"
    }), 201


# Get all skills of a user
@bp.route("/users/<userid>/skills", methods=["GET"])
def get_skills(userid):

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM skills
    WHERE userid = %s
    """

    cursor.execute(query, (userid,))

    skills = cursor.fetchall()

    cursor.close()

    return jsonify(skills)


# Get one skill
@bp.route("/skills/<skill_id>", methods=["GET"])
def get_skill(skill_id):

    cursor = db.cursor(dictionary=True)

    query = """
    SELECT * FROM skills
    WHERE skill_id = %s
    """

    cursor.execute(query, (skill_id,))

    skill = cursor.fetchone()

    cursor.close()

    return jsonify(skill)


# Update skill
@bp.route("/skills/<skill_id>", methods=["PUT"])
def update_skill(skill_id):

    data = request.get_json()

    skill_name = data["skill_name"]
    proficiency = data["proficiency"]
    category = data["category"]

    cursor = db.cursor()

    query = """
    UPDATE skills
    SET skill_name = %s,
        proficiency = %s,
        category = %s
    WHERE skill_id = %s
    """

    cursor.execute(
        query,
        (
            skill_name,
            proficiency,
            category,
            skill_id
        )
    )

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Skill updated!"
    })


# Delete skill
@bp.route("/skills/<skill_id>", methods=["DELETE"])
def delete_skill(skill_id):

    cursor = db.cursor()

    query = """
    DELETE FROM skills
    WHERE skill_id = %s
    """

    cursor.execute(query, (skill_id,))

    db.commit()
    cursor.close()

    return jsonify({
        "message": "Skill deleted!"
    })